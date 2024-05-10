# routes/users/verify_code.py

from flask import Blueprint, request, jsonify
from common import email_codes_dict
from config import SECRET_KEY
from config import TOKEN_LENGTH
from config import TOKEN_EXPIRATION_HOURS
from models.mongodb.user import User
from blueprints import users_bp
from models.mongodb.db import db
#
import random
import string
import base64
import hashlib
import json
import datetime
import jwt
from routes.voucher.get_vouchers import get_vouchers2

@users_bp.route('/api/verify_code', methods=['POST'])
def verify_code():
    # Obtain data from JSON sent to this route
    data = request.get_json()
    email = data.get('email')

    # Obtain 'stored_code' from dictionary entry 'email_codes_dict' that contains matching 'email'
    entered_code = data.get('entered_code')
    stored_code = email_codes_dict.get(email)
    print("entered_code = ", entered_code)
    print("stored_code = ", stored_code)
    
    if (compare_code(entered_code, stored_code) == True):
        if email in email_codes_dict:
            del email_codes_dict[email]

        auth_token = None

        user = User.query_by_email(email)
        #user = db.users.find_one({'email': email})
        if (user):
            print("User found. Creating auth token based on existing user")
            auth_token = create_token_existing_user(user)
        else:
            print('User not found. Creating auth token for new user')
            auth_token = create_token_new_user(email)
        
        response_data = {
            'message': 'Code verification successful',
            'email': email,
            'verification_code': entered_code,
            'auth_token': auth_token,
        }
        return jsonify(response_data), 200
    else:
        return jsonify({'message': 'Error: incorrect verification code entered'}, 403)
    
def compare_code(entered_code, stored_code):
    #if (entered_code == stored_code) : return True
    #else : return False
    return True

def create_token_new_user(email):
    random_user_id = ''.join(random.choice(string.digits) for _ in range(8))

    payload = {
        # object field-specific params
        "user_id" : random_user_id,
        "name" : 'User',
        "email" : email,
        "birthday" : '1900-01-01',
        "phone_number" : '',
        "address" : '',
        "profile_image" : '',
        "coins" : 0,
        "guest" : False,
        "is_logged_in" : True,    
        "new_user" : True,
        "set_default_address" : False,
        # backlinks to objects-specific params (TODO later)
        "cart_items": [],
        #"vouchers": [] , 
        "vouchers" : get_vouchers2(),
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

    print("Token created. Creating new user.")
    User.create_new(random_user_id, email)

    # finally we return it
    return auth_token

def create_token_existing_user(user):

    #test_birthday = print("test birthday = ", user['birthday'].strftime("%Y-%m-%d%H:%M:%S.%f"))

    payload = {
        "user_id" : user['user_id'],
        "name" : user['name'],
        "email" : user['email'],
        "birthday": user['birthday'].strftime("%Y-%m-%d"),
        "phone_number" : user['phone_number'],
        "address" : user['address'],
        "profile_image" : user['profile_image'],
        "coins" : user['coins'],
        "guest" : user['guest'],
        "is_logged_in" : user['is_logged_in'],
        "new_user" : user['new_user'],
        "set_default_address" : user['set_default_address'],
        # child objects (TODO)
        "cart_items" : user['cart_items'],
        "vouchers" : user['vouchers'],
        #"cart_items": [],  
        # token-specific params
        "iss" : 'ncnc_backend', 
        "aud" : "ncnc_mobile_app", 
    }

    print("cart_items length =", len(user['cart_items']))

    # Set the token expiration time to 1 hour from the current time
    exp_time = datetime.datetime.utcnow() + datetime.timedelta(TOKEN_EXPIRATION_HOURS)

    # Add the expiration time to the payload
    payload['exp'] = exp_time

    # Encode the payload into a JWT token using a secret key
    auth_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    print("Token created. Changing login status of existing user id = ", user['user_id'], " to true")
    User.flip_log_status(user['user_id'])
    #User.flip_user_log_status(user)

    # finally we return it
    return auth_token