# routes/cartitem/add_cartitem.py

from flask import Flask, Blueprint, jsonify, request
from models.mongodb.db import db
from models.mongodb.cartitem import CartItem
from models.mongodb.menuitem import MenuItem
from models.mongodb.user import User
from blueprints import cartitem_bp

# Adds a CartItem object to an existing entry in 'users' collection
@cartitem_bp.route('/add_cartitem', methods=['POST'])
def add_cartitem():
    json = request.json

    user = db.users.find_one({'user_id': json.get('user_id')})
    if user:
        user['cart_items'].append({
                'id': json.get('id'),
                'quantity': json.get('quantity'),
                'price': json.get('price'),
                'menuitem_id': json.get('menuitem_id'),
                'menuitem': json.get('menuitem')
        })
        # Update the user in the collection
        db.users.update_one({'user_id': json.get('user_id')}, {'$set': user})
        return jsonify({'message': 'CartItem added successfully'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404