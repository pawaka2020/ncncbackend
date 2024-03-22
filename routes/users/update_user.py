# routes/users/update_user.py

from flask import Blueprint, request, jsonify
from models.mongodb.user import User
from blueprints import users_bp
from models.mongodb.db import db

# Update user in 'users' collection
@users_bp.route('/api/update_user', methods=['POST'])
def update_user():
    # Obtain data from JSON sent to this route
    json_data = request.get_json()

    # Find the user in the database
    user = db.users.find_one({'user_id': json_data.get('user_id')})

    if user:
        # Update user fields with new data from JSON
        user['name'] = json_data.get('name')
        user['email'] = json_data.get('email')
        user['birthday'] = json_data.get('birthday')
        user['phone_number'] = json_data.get('phone_number')
        user['address'] = json_data.get('address')
        user['profile_image'] = json_data.get('profile_image')
        user['coins'] = json_data.get('coins')
        user['guest'] = json_data.get('guest')
        user['is_logged_in'] = json_data.get('is_logged_in')
        user['new_user'] = json_data.get('new_user')
        user['set_default_address'] = json_data.get('set_default_address')

        # Save the updated user object back to the database
        db.users.update_one({'user_id': json_data.get('user_id')}, {'$set': user})

        return jsonify({'message': 'User updated successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404