from flask import Blueprint, request, jsonify
from common import verification_codes
from models.user import find_registered_user
from models.user import create_new_user
from models.user import flip_user_log_status
from config import SECRET_KEY
from config import TOKEN_LENGTH
from config import TOKEN_EXPIRATION_HOURS
#
import random
import string
import base64
import hashlib
import json
import datetime
import jwt

verify_code_bp = Blueprint('verify_code', __name__)

@verify_code_bp.route('/api/verify_code', methods=['POST'])
def verify_code():
    data = request.get_json()
    phone_number = data.get('phone_number')
    entered_code = data.get('entered_code')

    # obtain 'stored_code' from dictionary entry 'verification_codes' that contains matching 'phone_number'
    stored_code = verification_codes.get(phone_number)

    auth_token = None

    if stored_code and stored_code == entered_code:
        print("stored code", stored_code, "matches entered code", entered_code)
        user = find_registered_user(phone_number)
        if (user):
            print("User found. Creating auth token based on existing user")
            auth_token = create_token_existing_user(user)
            
        else:
            print('User not found. Creating auth token for new user')
            auth_token = create_token_new_user(phone_number)
            
        response_data = {
            'message': 'Code verification successful',
            'phone_number': phone_number,
            'verification_code': entered_code,
            'auth_token': auth_token,
        }
        return jsonify(response_data), 200
    else:
        print("Error: stored code", stored_code, "does not match entered code", entered_code)
        return jsonify({'message': 'Code verification failed'}), 400     

def create_token_new_user(phone_number):

    random_user_id = ''.join(random.choice(string.digits) for _ in range(8))

    payload = {
        #object field-specific params
        "user_id" : random_user_id,
        "phone_number" : phone_number,
        "guest" : False,
        "new_user" : True,
        # backlinks to objects-specific params (TODO later)
        # token-specific params
        "iss" : 'ncnc_backend', 
        "aud" : "ncnc_mobile_app", 
    }

    # Set the token expiration time to 1 hour from the current time
    exp_time = datetime.datetime.utcnow() + datetime.timedelta(TOKEN_EXPIRATION_HOURS)

    # Add the expiration time to the payload
    payload['exp'] = exp_time

    # Encode the payload into a JWT token using a secret key
    auth_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    print("Token created. Creating new user in postgreSQL table")
    create_new_user(random_user_id, phone_number)

    # finally we return it
    return auth_token

def create_token_existing_user(user):
    payload = {
        "user_id" : user.user_id,
        "phone_number" : user.phone_number,
        "guest" : user.guest,
        "new_user" : False,
        # backlinks to objects-specific params (TODO later)
        # token-specific params
        "iss" : 'ncnc_backend', 
        "aud" : "ncnc_mobile_app", 
    }
    # Set the token expiration time to 1 hour from the current time
    exp_time = datetime.datetime.utcnow() + datetime.timedelta(TOKEN_EXPIRATION_HOURS)

    # Add the expiration time to the payload
    payload['exp'] = exp_time

    # Encode the payload into a JWT token using a secret key
    auth_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    print("Token created. Changing login status of existing user to true")
    flip_user_log_status(user)

    # finally we return it
    return auth_token