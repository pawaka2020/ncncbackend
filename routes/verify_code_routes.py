#routs/verify_code_routes.py
from flask import Blueprint, request, jsonify

verify_code_bp = Blueprint('verify_code', __name__)

@verify_code_bp.route('/api/verify_code', methods=['POST'])
def verify_code():
    data = request.get_json()
    phone_number = data.get('phone_number')
    entered_code = data.get('entered_code')

    #logic block to compare 'entered_code' with 'generated_code' that matches 'phone_number'


    return jsonify({'message': 'Verification code received successfully'}), 200