# plaid-poc
Plaid Technical Challenge

## Project Overview

This repository contains the backend code for the Bank Account Connection module. The main purpose of this module is to allow users to connect their bank accounts securely using Plaid, retrieve their financial data, and store it in Firebase Firestore.

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

![3](https://github.com/techchallenger7765/plaid-poc/assets/146533891/05d8935d-514e-41c8-8a13-14283520894f)

![4](https://github.com/techchallenger7765/plaid-poc/assets/146533891/41c4aaf6-38b9-4ae2-a1d2-36e2bfd64fde)

![2](https://github.com/techchallenger7765/plaid-poc/assets/146533891/10d4d697-013c-4361-8e70-101ed1ddebd7)

![1](https://github.com/techchallenger7765/plaid-poc/assets/146533891/bf502a2d-2876-41c9-9ce0-4c615c3a9dc4)


## License
Copyright free

## Acknowledgments

- Thanks for the challenge.
