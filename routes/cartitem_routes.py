#routes/cartitem_routes.py

from flask import Blueprint, jsonify
from models.cartitem import CartItem

cartitem_bp = Blueprint('cartitem_bp', __name__)

@cartitem_bp.route('/cartitems', methods=['GET'])
def get_cartitem():
    cartitems = CartItem.query.all()
    # # Serialize cartitems to JSON
    serialized_cartitems = [cartitem.serialize() for cartitem in cartitems]
    return jsonify(serialized_cartitems), 200