# routes/cartitem/delete_cartitem.py

from flask import Flask, Blueprint, jsonify, request
from models.mongodb.db import db
from models.mongodb.cartitem import CartItem
from models.mongodb.menuitem import MenuItem
from models.mongodb.user import User
from blueprints import cartitem_bp

# Edits CartItem object from an existing entry in 'users' collection
@cartitem_bp.route('/edit_cartitem', methods=['POST'])
def edit_cartitem():
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
                # Update the cart item with new data
                cart_item.update({
                    'quantity': json_data.get('quantity', cart_item.get('quantity')),
                    'price': json_data.get('price', cart_item.get('price')),
                    'menuitem_id': json_data.get('menuitem_id', cart_item.get('menuitem_id')),
                    'menuitem': json_data.get('menuitem', cart_item.get('menuitem'))
                })
                break
        
        # Update the user in the collection
        db.users.update_one({'user_id': user_id}, {'$set': {'cart_items': cart_items}})
        return jsonify({'message': 'CartItem edited successfully'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404