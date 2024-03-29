from flask import Blueprint, jsonify, request
from models.user import User
from blueprints import user_bp
from models.db import db
#
from models.cartitem import CartItem

@user_bp.route('/edit_cart_user', methods=['POST'])
def edit_cart_user():
    json = request.json
    
    # Extract data from json
    user_id_ = json.get('user_id')
    cartitem_ = CartItem.from_json(json)
    ### cartitem_ = json.get('cartitems')

    # Check if required data is provided
    if not user_id_ or not cartitem_:
        return jsonify({'error': 'Invalid request data'}), 400

    # Find the user
    user = User.query.filter_by(user_id=user_id_).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    # Find the cart item associated with the user
    cartitem = CartItem.query.filter_by(id=cartitem_.id, user_id=user.id).first()
    if not cartitem:
        return jsonify({'error': 'Cart item not found for the user'}), 404

    # Update cart item attributes
    cartitem.price = cartitem_.price
    cartitem.quantity = cartitem_.quantity

    try:
        db.session.commit()
        return jsonify({'message': 'Cart item updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to update cart item', 'details': str(e)}), 500