# routes/users/get_users.py

from flask import Blueprint, jsonify
from models.user import User

get_users_bp = Blueprint('get_users_bp', __name__)

# @get_users_bp.route('/get_users', methods=['GET'])
# def get_users():
#     users = User.query.all()
#     user_list = []
#     for user in users:

#         # Retrieve associated cart items for the user
#         cart_items = [cart_item.price for cart_item in user.cartitem]

#         user_data = {
#             'id': user.id,
#             'user_id': user.user_id,
#             'name': user.name,
#             'email': user.email,
#             'birthday': str(user.birthday) if user.birthday else None,
#             'phone_number': user.phone_number,
#             'address': user.address,
#             'profile_image': user.profile_image,
#             'coins': user.coins,
#             'guest': user.guest,
#             'is_logged_in': user.is_logged_in,
#             'new_user': user.new_user,
#             'set_default_address': user.set_default_address,
#             'cart_items': cart_items
#             # Add more fields as needed
#         }
#         user_list.append(user_data)
#     #return jsonify({'users': user_list})
#     return jsonify(user_list)

@get_users_bp.route('/get_users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        cart_items = []

        # Retrieve associated cart items for the user
        for cart_item in user.cartitem:
            cart_item_data = {
                'price' : cart_item.price,
                'quantity' : cart_item.quantity,
                # Add more fields if needed
            }
            cart_items.append(cart_item_data)

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
            'set_default_address': user.set_default_address,
            'cart_items': cart_items
            # Add more fields as needed
        }
        user_list.append(user_data)
    return jsonify(user_list)

# TODO: Add backlinks later