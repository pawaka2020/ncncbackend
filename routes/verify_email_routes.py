from flask import Blueprint, request, jsonify
import random
from common import email_codes_dict
from utils.send_email import send_email

verify_email_bp = Blueprint('verify_email', __name__)

@verify_email_bp.route('/api/verify_email', methods=['POST'])
def verify_email_number():
    # Obtain data from JSON sent to this route
    data = request.get_json()
    email = data.get('email')

    # Generate a 4-digit code
    verification_code = generate_verification_code()
    print("Received email =", email)
    print("Generated code = ", verification_code)

    # Store the verification code 
    email_codes_dict[email] = verification_code
    print("Stored code = ", email_codes_dict.get(email))

    # Send email to 'email' containing 'verification_code' (TODO)
    send_email(email, 'Hello World')

    return jsonify({'message': 'Phone number received successfully'}), 200

def generate_verification_code():
    # Generate a 4-digit random code
    verification_code = ''.join(random.choices('0123456789', k=4))
    return verification_code

def send_verification_code_email(verification_code, phone_number):
    print("TODO");