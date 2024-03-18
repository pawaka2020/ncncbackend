from flask import Blueprint, jsonify, request
from models.user import User
from blueprints import user_bp
from models.db import db
#
from models.cartitem import CartItem

# def add_menuitem_cartitem():
#     print("TODO")

# @user_bp.route('/add_cart_user', methods=['POST'])
# def add_cart_user():
#     # Parse JSON data received from POST request
#     data = request.json
#     user_id_ = data.get('user_id') 
#     price_ = data.get('price')
#     quantity_ = data.get('quantity')

#     # Find a 'User' object from 'users' PostgreSQL table by matching 'user_id_'
#     user = User.query.filter_by(user_id=user_id_).first()

#     if user:
#         # Edit this 'User' object by appending a 'CartItem' object to it with values fetched from JSON
#         user.cartitem.append(
#             CartItem(
#                 quantity = quantity_,
#                 price = price_,
#                 # menuitem = add_menuitem_cartitem() // I'll do this later
#             )    
#         )
#         # Commit the changed 'User' object to 'users' table
#         db.session.commit()

#         return jsonify({'message': 'Cart item added to user successfully'})   
#     else:
#         # Return response and don't do anything else. 
#         return jsonify({'error': 'User not found'}), 404

@user_bp.route('/add_cart_user', methods=['POST'])
def add_cart_user(): 
    json = request.json

    user_id_ = json.get('user_id')
    cartitem_ = CartItem.from_json(json)
    
    user = User.query.filter_by(user_id=user_id_).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    if user:
        user.cartitem.append(cartitem_)
        db.session.commit()

        return jsonify({'message': 'Cart item added to user successfully'})   
    else:
        return jsonify({'error': 'User not found'}), 404