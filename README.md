# plaid-poc
Plaid Technical Challenge

## Project Overview

This repository contains the backend code for the Bank Account Connection module of Budgetwise. The main purpose of this module is to allow users to connect their bank accounts securely using Plaid, retrieve their financial data, and store it in Firebase Firestore.

## Technologies Used

- Python
- Django
- Plaid API
- Firebase Firestore

# Key Info

**Plaid Integration:**
   - Integrated Plaid Link into your frontend application to enable users to securely connect their bank accounts.
   - Handled user authentication and stored Plaid access tokens securely.

**Retrieve and Store Data:**
   - Used Plaid API endpoints to retrieve users' financial data, such as account balances and transaction history.
   - Routed the data into Firebase Firestore for storage.


## Project Structure

The project is organized as follows:

- `budgetwise_backend/`: Django application for the backend.
- `requirements.txt`: List of project dependencies.
- `manage.py`: Django management script.
- `Procfile`: Heroku deployment configuration (if applicable).
- `README.md`: This documentation.

## Getting Started

1. **Set Up Developer Account with Plaid:**
   - Sign up for a developer account with Plaid (https://plaid.com/).
   - Obtain your Plaid API keys and credentials.

2. **Configuration:**
   - Update the Plaid API credentials in `budgetwise_backend/settings.py` using `PLAID_CLIENT_ID` and `PLAID_SECRET_ID`.

## Project Usage

- Access the application by running the Django development server.
- Users can connect their bank accounts through Plaid Link.
- The application retrieves and stores users' financial data in Firestore.

## Screenshots
![3](https://github.com/techchallenger7765/plaid-poc/assets/146533891/841b7590-fc9b-4878-bd5e-37403d6de5b6)

![4](https://github.com/techchallenger7765/plaid-poc/assets/146533891/6bec797b-93ed-4202-bfb6-565fc0afe756)

![2](https://github.com/techchallenger7765/plaid-poc/assets/146533891/3f549191-c4cb-4f97-866a-6f259b08c22b)

![1](https://github.com/techchallenger7765/plaid-poc/assets/146533891/dc4210de-81bc-4d21-8064-9512ee6216e4)


## License
Copyright free

## Acknowledgments

- Thanks for the challenge.
