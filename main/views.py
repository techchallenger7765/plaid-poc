# Create your views here.

import plaid
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from firebase_admin import db
from plaid.api import plaid_api
from plaid.model.auth_get_request import AuthGetRequest
from plaid.model.country_code import CountryCode
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
from plaid.model.link_token_create_request import LinkTokenCreateRequest
from plaid.model.link_token_create_request_user import LinkTokenCreateRequestUser
from plaid.model.products import Products

from POCPlaid.settings import PLAID_CLIENT_ID, PLAID_SECRET_ID

configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': PLAID_CLIENT_ID,
        'secret': PLAID_SECRET_ID,
    }
)
api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

ref = db.reference('/', url="https://plaid-project-a350e-default-rtdb.firebaseio.com/")


@csrf_exempt
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def fetch_token(request):
    """
        Calls plaid api to generate
        a link token which will be later
        used to authenticate and open
        plaid's modal
        :param request: received request
        :return: link_token received from plaid
        """
    try:
        request = LinkTokenCreateRequest(
            products=[Products("auth")],
            client_name="Wallet Watch",
            country_codes=[CountryCode('US')],
            language='en',
            user=LinkTokenCreateRequestUser(client_user_id=str(request.user.id))
        )

        response = client.link_token_create(request)
        return JsonResponse(response.to_dict())
    except Exception as e:
        print(e)
        return HttpResponseForbidden(str(e))


def save_to_firebase(data):
    new_data_ref = ref.push(data)
    new_key = new_data_ref.key
    print(f'Data saved with key: {new_key}')


@csrf_exempt
def verify_and_save_bank_account(request):
    """
    Retrieves the access token from plaid,
    saves it against the default user. This
    access token will be used to communicate
    with plaid's API
    """
    if request.method == 'POST':
        try:
            public_token = request.POST.get('public_token')

            # Exchange the public token for access token
            plaid_request = ItemPublicTokenExchangeRequest(
                public_token=public_token
            )
            exchange_response = client.item_public_token_exchange(plaid_request)

            access_token = exchange_response["access_token"]
            auth_response = fetch_account_info(access_token)

            save_to_firebase(data={
                "user_id": request.user.id,
                "access_token": access_token,
                "auth_info": auth_response
            })

            return redirect('/')
        except Exception as e:
            print(e)
            return HttpResponseForbidden(str(e))
    else:
        return HttpResponseForbidden("Permission denied")


def fetch_account_info(access_token):
    """
        Fetch account info from Plaid against a user
    """
    request = AuthGetRequest(access_token=access_token)
    response = client.auth_get(request)
    return serialize_auth_response(response)


def serialize_auth_response(response_data):
    serialized_data = {
        'account_summaries': [],
        'item_info': {
            'item_id': response_data['item']['item_id'],
            'institution_id': response_data['item']['institution_id']
        },
        'ach_accounts': [],
        'eft_accounts': [],
        'international_accounts': [],
        'bacs_accounts': []
    }

    # Extract and serialize account information
    for account in response_data['accounts']:
        account_summary = {
            'account_id': account['account_id'],
            'name': account['name'],
            'current_balance': account['balances']['current']
        }
        serialized_data['account_summaries'].append(account_summary)

    # Extract and serialize ACH account information
    for ach_account in response_data['numbers']['ach']:
        ach_info = {
            'account_id': ach_account['account_id'],
            'account_number': ach_account['account'],
            'routing_number': ach_account['routing']
        }
        serialized_data['ach_accounts'].append(ach_info)

    # Extract and serialize EFT account information
    for eft_account in response_data['numbers']['eft']:
        eft_info = {
            'account_id': eft_account['account_id'],
            'account_number': eft_account['account'],
            'institution': eft_account['institution'],
            'branch': eft_account['branch']
        }
        serialized_data['eft_accounts'].append(eft_info)

    # Extract and serialize international account information
    for international_account in response_data['numbers']['international']:
        international_info = {
            'account_id': international_account['account_id'],
            'bic': international_account['bic'],
            'iban': international_account['iban']
        }
        serialized_data['international_accounts'].append(international_info)

    # Extract and serialize BACS account information
    for bacs_account in response_data['numbers']['bacs']:
        bacs_info = {
            'account_id': bacs_account['account_id'],
            'account_number': bacs_account['account'],
            'sort_code': bacs_account['sort_code']
        }
        serialized_data['bacs_accounts'].append(bacs_info)

    return serialized_data
