# routes/user_routes.py

from flask import Blueprint, jsonify
from models.user import User

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_data = {
            'id': user.id,
            'user_id': user.user_id,
            'name': user.name,
            'email': user.email,
            'birthday': str(user.birthday) if user.birthday else None,
            'phone_number': user.phone_number,
            'address': user.address,
            'profile_image': user.profile_image,
            'coins': user.coins,
            'guest': user.guest,
            'is_logged_in': user.is_logged_in,
            'new_user': user.new_user,
            'set_default_address': user.set_default_address
            # Add more fields as needed
        }
        user_list.append(user_data)
    #return jsonify({'users': user_list})
    return jsonify(user_list)

# TODO: Add backlinks later