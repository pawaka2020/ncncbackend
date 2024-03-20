# routes/cartitem/delete_cartitem.py

from flask import Flask, Blueprint, jsonify, request
from models.mongodb.db import db
from models.mongodb.cartitem import CartItem
from models.mongodb.menuitem import MenuItem
from models.mongodb.user import User
from blueprints import cartitem_bp

# Edits CartItem object from an existing entry in 'users' collection
@cartitem_bp.route('/edit_cartitem', methods=['POST'])
def delete_cartitem():
    print("TODO")