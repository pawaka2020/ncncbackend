# routes/cartitem/get_cartitem.py

from flask import Blueprint, jsonify
from models.cartitem import CartItem

get_cartitem_bp = Blueprint('get_cartitem_bp', __name__)

@get_cartitem_bp.route('/get_cartitems', methods=['GET'])
def get_cartitems() :
    cart_items = CartItem.query.all()
    cart_item_list = []

    for cart_item in cart_items:
        cart_item_data = {
            'id': cart_item.id,
            'content': cart_item.content,
            'quantity': cart_item.quantity,
            'menuitem_id': cart_item.menuitem_id,
            'price': cart_item.price,
            'user_id': cart_item.user_id
            # Add more fields as needed
        }
        cart_item_list.append(cart_item_data)

    return jsonify(cart_item_list)