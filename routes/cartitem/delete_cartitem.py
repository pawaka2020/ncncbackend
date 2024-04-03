# routes/cartitem/delete_cartitem.py

from flask import Flask, Blueprint, jsonify, request
from models.mongodb.db import db
from models.mongodb.cartitem import CartItem
from models.mongodb.menuitem import MenuItem
from models.mongodb.user import User
from blueprints import cartitem_bp

# Removes CartItem object from an existing entry in 'users' collection
@cartitem_bp.route('/delete_cartitem', methods=['POST'])
def delete_cartitem():
    json_data = request.json

    user_id = json_data.get('user_id')
    cartitem_id = json_data.get('id')

    if not user_id or not cartitem_id:
        return jsonify({'error': 'Invalid request data'}), 400
    
    # Find user in 'users' collection using matching 'user_id'
    user = db.users.find_one({'user_id': user_id})
    
    if user:
        # Find 'cart_items' in 'users' collection using matching 'id'
        cart_items = user.get('cart_items', [])
        for cart_item in cart_items:
            if cart_item.get('id') == cartitem_id:
                # Delete the 'cart_item' object from the 'cart_items' list
                cart_items.remove(cart_item)
                break
        
        # Update the user in the collection
        db.users.update_one({'user_id': user_id}, {'$set': {'cart_items': cart_items}})
        return jsonify({'message': 'CartItem deleted successfully'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404