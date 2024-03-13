# routes/users/update_user.py
from flask import Blueprint, jsonify, request
from models.user import User
from models.db import db
#
from models.cartitem import CartItem

update_user_bp = Blueprint('update_user_bp', __name__)

# @update_user_bp.route('/update_user', methods=['POST'])
# def update_user():
#     # Parse JSON data from Flutter app
#     data = request.json

#     # Retrieve class field values from JSON data
#     id = data.get('user_id')
#     new_address = data.get('new_address')
#     new_name = data.get('new_name')
#     new_email = data.get('new_email')
#     new_birthday = data.get('new_birthday')
#     new_phone_number = data.get('new_phone_number')
#     new_profile_image = data.get('new_profile_image')
#     new_coins = data.get('new_coins')
#     new_guest = data.get('new_guest').lower() == 'true'
#     new_is_loggged_in = data.get('new_is_logged_in').lower() == 'true'
#     new_new_user = data.get('new_new_user').lower() == 'true'
#     new_set_default_address = data.get('new_set_default_address').lower() == 'true'
    
#     # Find the user by user_id
#     user = User.query.filter_by(user_id=id).first()

#     if user:
#         # Update the proprietary fields of user
#         user.address = new_address
#         user.name = new_name
#         user.email = new_email
#         user.birthday = new_birthday
#         user.phone_number = new_phone_number
#         user.profile_image = new_profile_image
#         user.coins = new_coins
#         user.guest = new_guest
#         user.is_logged_in = new_is_loggged_in
#         user.new_user = new_new_user
#         user.set_default_address = new_set_default_address
    
#         # cart_item_data = data.get('cart_item')
#         # if cart_item_data:
#         #     price = float(cart_item_data.get('price'))  # Convert price to float
#         #     cart_item = CartItem(price=price)
#         #     user.cartitem.append(cart_item)

#         user.cartitem.append(CartItem(price = '20'))
#         user.cartitem.append(CartItem(price = '25'))
#         user.cartitem.append(CartItem(price = '30'))

#         db.session.commit()
#         print("User updated successfully")
#         return jsonify({'message': 'User updated successfully'})
#     else:
#         return jsonify({'error': 'User not found'}), 404

def update_cart_items(user, cart_items_data):
  # Clear existing cart items
  user.cartitem[:] = []

    # Add new cart items if data is provided
  if cart_items_data:
    for item_data in cart_items_data:
      price = item_data.get('price')
      quantity = item_data.get('quantity')
      user.cartitem.append(CartItem(
        price=price,
        quantity=quantity
      ))

def update_cart_items2(user, cart_items_data):
    # I actually want to delete existing 'cartitem' rows that link to this current 'users' row first.
    # ????
    # Create a list to hold the new cart items
    new_cart_items = []

    # Add new cart items if data is provided
    if cart_items_data:
        for item_data in cart_items_data:
            price = item_data.get('price')
            quantity = item_data.get('quantity')
            new_cart_items.append(CartItem(
                price=price,
                quantity=quantity
        ))

    return new_cart_items

@update_user_bp.route('/update_user', methods=['POST'])
def update_user():
    # Parse JSON data from Flutter app
    data = request.json

    # Retrieve class field values from JSON data
    id = data.get('user_id')
    new_address = data.get('new_address')
    new_name = data.get('new_name')
    new_email = data.get('new_email')
    new_birthday = data.get('new_birthday')
    new_phone_number = data.get('new_phone_number')
    new_profile_image = data.get('new_profile_image')
    new_coins = data.get('new_coins')
    new_guest = data.get('new_guest').lower() == 'true'
    new_is_logged_in = data.get('new_is_logged_in').lower() == 'true'
    new_new_user = data.get('new_new_user').lower() == 'true'
    new_set_default_address = data.get('new_set_default_address').lower() == 'true'
    
    # Find the user by user_id
    user = User.query.filter_by(user_id=id).first()

    if user:
        # Update the proprietary fields of user
        user.address = new_address
        user.name = new_name
        user.email = new_email
        user.birthday = new_birthday
        user.phone_number = new_phone_number
        user.profile_image = new_profile_image
        user.coins = new_coins
        user.guest = new_guest
        user.is_logged_in = new_is_logged_in
        user.new_user = new_new_user
        user.set_default_address = new_set_default_address

        # Remove existing cart items
                # Remove existing cart items
        # user.cartitem[:] = []
        # # Check if cart items data is provided
        # cart_items_data = data.get('cart_items')
        # if cart_items_data:
        #   for item_data in cart_items_data:
        #     price = item_data.get('price')
        #     quantity = item_data.get('quantity')
        #     user.cartitem.append(CartItem(
        #       price=price, 
        #       quantity=quantity
        #       )
        #     )
        
        # Update cart items
        #update_cart_items(user, data.get('cart_items'))
        # user.cartitem = update_cart_items2(user, data.get('cart_items'))
        # Update cart items directly
        user.cartitem = update_cart_items2(user, data.get('cart_items'))
        db.session.commit()
        print("User updated successfully")
        return jsonify({'message': 'User updated successfully'})
    else:
        return jsonify({'error': 'User not found'}), 404

{
  "user_id": "123456",
  "new_address": "123 Main St",
  "new_name": "John Doe",
  "new_email": "john@example.com",
  "new_birthday": "1990-01-01",
  "new_phone_number": "123-456-7890",
  "new_profile_image": "profile.jpg",
  "new_coins": 100,
  "new_guest": "true",
  "new_is_logged_in": "false",
  "new_new_user": "true",
  "new_set_default_address": "false",
  "cart_items": [
    {
      "price": 20.0
    },
    {
      "price": 25.0
    },
    {
      "price": 30.0
    }
  ]
}
