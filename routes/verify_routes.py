from flask import Blueprint, request, jsonify
#from models.db import redis_client
import random
from common import verification_codes

#verify_bp = Blueprint('verify', __name__)

# @verify_bp.route('/api/verify', methods=['POST'])
# def verify_phone_number():
#     data = request.get_json()
#     phone_number = data.get('phone_number')

#     # Generate a 4-digit code (TODO)
#     verification_code = generate_verification_code()

#     # Store the verification code in Redis with a short expiration time (e.g., 1 minute)
#     redis_client.setex(phone_number, 60, verification_code)

#     return jsonify({'message': 'Phone number and verification code received successfully'}), 200

# def generate_verification_code():
#     # Generate a 4-digit random code
#     verification_code = ''.join(random.choices('0123456789', k=4))
#     return verification_code

verify_bp = Blueprint('verify', __name__)

@verify_bp.route('/api/verify', methods=['POST'])
def verify_phone_number():
    data = request.get_json()
    phone_number = data.get('phone_number')

    # Generate a 4-digit code (TODO)
    verification_code = generate_verification_code()
    print("Received phone number =", phone_number)
    print("Generated code = ", verification_code)

    # Store the verification code 
    verification_codes[phone_number] = verification_code
    print("Stored code = ", verification_codes.get(phone_number))

    return jsonify({'message': 'Phone number received successfully'}), 200

def generate_verification_code():
    # Generate a 4-digit random code
    verification_code = ''.join(random.choices('0123456789', k=4))
    return verification_code