#routes/verify_routes.py
from flask import Blueprint, request, jsonify

verify_bp = Blueprint('verify', __name__)

@verify_bp.route('/api/verify', methods=['POST'])
def verify_phone_number():
    data = request.get_json()
    phone_number = data.get('phone_number')

    # Print the phone number to view it in the Flask console
    print("Received phone number:", phone_number)
    # Generate a 4-digit code (TODO)

    return jsonify({'message': 'Phone number received successfully'}), 200