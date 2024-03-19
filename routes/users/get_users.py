# routes/users/get_users.py

from flask import Flask, Blueprint, jsonify
from models.mongodb.db import db
from models.mongodb.user import User
from blueprints import users_bp

# Displays all objects of User in JSON format on the browser
@users_bp.route('/get_users', methods=['GET'])
def get_users():
    users_list = list(db['users'].find({}))

    result = [{
        'address': user['address'],
        'birthday': user['birthday'],
        'cart_items': user['cart_items'],
        'orders': user['orders'],
        'coins': user['coins'],
        'email': user['email'],
        'guest': user['guest'],
        'id': user['id'],
        'is_logged_in': user['is_logged_in'],
        'name': user['name'],
        'new_user': user['new_user'],
        'phone_number': user['phone_number'],
        'profile_image': user['profile_image'],
        'set_default_address': user['set_default_address'],
        'user_id': user['user_id']
    } for user in users_list]

    return jsonify(result)

