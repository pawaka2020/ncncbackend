# routes/users/request_code.py

from flask import Flask, Blueprint, jsonify, request
from models.mongodb.db import db
from models.mongodb.user import User
from blueprints import users_bp
import random
from common import email_codes_dict
from utils.send_email import send_email

@users_bp.route('/api/request_code', methods=['POST'])
def request_code():
    # Obtain data from JSON
    data = request.get_json()
    email = data.get('email')

    # Generate 4-digit code
    verification_code = ''.join(random.choices('0123456789', k=4))
    email_codes_dict[email] = verification_code
    print("Received email = ", email)
    print("Verification code = ", verification_code)

    return jsonify({'message': 'Phone number received successfully'}), 200