from flask import Blueprint, jsonify, request
from models.user import User
from blueprints import user_bp
from models.db import db
#
from models.cartitem import CartItem

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