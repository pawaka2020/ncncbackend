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
    json = request.json

    user_id = json.get('user_id')
    id = json.get('id')

    if not user_id or not  id:
        return jsonify({'error': 'Invalid request data'}), 400
    
    # finds user in 'users' collection using matching 'user_id'


    print("TODO")