from flask import Blueprint, jsonify, request
from models.user import User
from blueprints import user_bp
from models.db import db
#
from models.cartitem import CartItem

@user_bp.route('/delete_cart_user', methods=['POST'])
def delete_cart_user():
    json = request.json

    user_id_ = json.get('user_id')
    id_ = json.get('id')

    if not user_id_ or not  id_:
        return jsonify({'error': 'Invalid request data'}), 400
    
    user = User.query.filter_by(user_id=user_id_).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    # Find the cart item associated with the user
    cartitem = CartItem.query.filter_by(id=id_, user_id=user.id).first()
    if not cartitem:
        return jsonify({'error': 'Cart item not found for the user'}), 404
    # Delete the cart item associated with the user
    try:
        db.session.delete(cartitem)
        db.session.commit()
        return jsonify({'message': 'Cart item deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete cart item', 'details': str(e)}), 500