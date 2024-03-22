# routes/users/logoff.py

from flask import Flask, Blueprint, jsonify, request
from models.mongodb.db import db
from models.mongodb.user import User
from blueprints import users_bp

# logs off user
@users_bp.route('/logoff', methods=['POST'])
def logoff():
    json_data = request.json

    user_id = json_data.get('user_id')
    if not user_id:
        return jsonify({'error': 'Invalid user id'}), 400
    
    user = db.users.find_one({'user_id': user_id})
    if user:
        User.flip_log_status(user_id)
        # return jsonify({'message': "User " + user_id + " logged off successfully"}), 200
        print("user found")
    else:
        # return jsonify({'message': 'User not found'}), 4999999904
        print("user not found")
    return jsonify({'message': "User " + user_id + " logged off successfully"}), 200