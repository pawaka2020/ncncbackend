# from flask import Blueprint, request, jsonify
# import random
# from common import verification_codes

# verify_bp = Blueprint('verify', __name__)

# @verify_bp.route('/api/verify', methods=['POST'])
# def verify_phone_number():
#     # Receive phone number from JSON sent to this route
#     data = request.get_json()
#     phone_number = data.get('phone_number')

#     # Generate a 4-digit code
#     verification_code = generate_verification_code()
#     print("Received phone number =", phone_number)
#     print("Generated code = ", verification_code)

#     # Store the verification code 
#     verification_codes[phone_number] = verification_code
#     print("Stored code = ", verification_codes.get(phone_number))

#     # Send SMS to user's phone containing verification_code (TODO)
#     # send_verification_code_SMS(verification_code, phone_number)

#     return jsonify({'message': 'Phone number received successfully'}), 200

# def generate_verification_code():
#     # Generate a 4-digit random code
#     verification_code = ''.join(random.choices('0123456789', k=4))
#     return verification_code