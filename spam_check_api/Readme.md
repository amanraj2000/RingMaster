# Spam Call Check API

This is a Django-based API that helps identify and manage spam phone numbers. It supports user registration, login, and maintains a contact list with spam reports.

## Prerequisites

Before running the project, following things need to be installed:

- Python 3.10+ 
- PostgreSQL
- pip 

## Setup Instructions

### 1. Create and activate a virtual environment:
(For Windows)
python -m venv venv
.\venv\Scripts\activate

(For Mac/Linux)
python3 -m venv venv
source venv/bin/activate

### 2. Install dependencies
pip install -r requirements.txt


### 3. Set Up DB in .env File

### 4. Test the APIs

## REGISTER - {POST} api/register
Sample: {
  "name": "Aman Raj",
  "phone_number": "9876543210",
  "password": "password123",
  "email": "amanraj@sample.com"
}

## LOGIN - {POST} api/login
Sample: {
  "phone_number": "9876543210",
  "password": "password123"
}

## SEARCH_NAME - {GET} api/search_name/:name

## SEARCH_PHONE_NUMBER - {GET} api/search_phone_number/:phone_number



