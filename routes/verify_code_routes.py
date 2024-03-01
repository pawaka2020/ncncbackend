from flask import Blueprint, request, jsonify
from common import verification_codes
from models.user import find_registered_user

verify_code_bp = Blueprint('verify_code', __name__)

@verify_code_bp.route('/api/verify_code', methods=['POST'])
def verify_code():
    data = request.get_json()
    phone_number = data.get('phone_number')
    entered_code = data.get('entered_code')

    stored_code = verification_codes.get(phone_number)

    # I check that stored_code matches entered_code.
    # Then once there is a match, I use phone number to search for an entry in 'user' table 
    # in PostgreSQL with matching phone_number, and also with value 'isLoggedIn' false
    # If entry not found, I conclude this is a new login and I create a token from scratch.
    # I auto-generate the 'user_id' and set 'guest' = true and 'newuser' = true
    # I attach 'user_id', 'guest', 'newuser', 'phone_number' as payloads to the new token.
    # I create the new entry in 'user' table using 'user_id', 'guest', 'newuser', 'phone_number' as the new entry's row values.
    # I change the entry's 'isLoggedIn' value to true.
    # I include the token to the return jsonify of this ('POST') method
    # If entry found, I conlude this is not a lew login and I create a token based on values from the table's entry.
    # I grab the 'user_id', 'guest', 'newuser', 'phone_number' values from the entry.
    # I attach 'user_id', 'guest', 'newuser', 'phone_number' as payloads to the new token.
    # I change the entry's 'isLoggedIn' value to true.
    # I include the token to the return jsonify of this ('POST') method

    if stored_code and stored_code == entered_code:
        print("stored code", stored_code, "matches entered code", entered_code)
        user = find_registered_user(phone_number)
        if (user):
            print("User found. Creating auth token based on existing user")
            print("Token created. Changing login status of existing user to true")
            # TODO: create a function to handle this.
        else:
            print('User not found')







        response_data = {
            'message': 'Code verification successful',
            'phone_number': phone_number,
            'verification_code': entered_code,
        }
        return jsonify(response_data), 200
    else:
        print("Error: stored code", stored_code, "does not match entered code", entered_code)
        return jsonify({'message': 'Code verification failed'}), 400
    
# TODO LIST:
# 1 - Create 'users' table in PostgreSQL (Done)
# 2 - Create logic to parse 'user' table
# 3 - Create logic to read 'user' table
# 4 - ?????

# find_registered_user(phone_number):
# find a entry in 'users' table that satisfies these two conditions:
# 1 - 'phone_number' parameter matches 'phone_numer' column in that entry.
# 2 - 'is_logged_in' column of that entry is already set to 'false'. 
# if such an entry is found, return ?????
# if such an entry is not found, return ??????