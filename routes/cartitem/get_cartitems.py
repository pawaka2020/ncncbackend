# routes/cartitem/get_cartitem.py

# from flask import Blueprint, jsonify
# from models.cartitem import CartItem

# get_cartitem_bp = Blueprint('get_cartitem_bp', __name__)

# @get_cartitem_bp.route('/get_cartitems', methods=['GET'])
# def get_cartitems() :
#     cart_items = CartItem.query.all()
#     cart_item_list = []

#     for cart_item in cart_items:
#         print ('title adasd = ', cart_item.menuitem)
#         cart_item_data = {
#             'id': cart_item.id,
#             'content': cart_item.content,
#             'quantity': cart_item.quantity,
#             'menuitem_id': cart_item.menuitem_id,
#             'price': cart_item.price,
#             'user_id': cart_item.user_id,
#             # 'menuitem' : [
#             #     {
#             #         'imagepath' : menu_item.imagepath,
#             #         'title' : menu_item.title,
#             #     } for menu_item in cart_item.menuitem
#             # ] if cart_item.menuitem else [],
#         }
#         cart_item_list.append(cart_item_data)

#     return jsonify(cart_item_list)

from flask import Flask, Blueprint, jsonify
from models.mongodb.db import db
from models.mongodb.cartitem import CartItem
from blueprints import cartitem_bp

# Displays all objects of CartItem in JSON format on the browser
@cartitem_bp.route('/get_cartitems', methods=['GET'])
def get_cartitems():
    cartitem_list = list(db['cartitems'].find({}))

    result = [{
        'quantity': cartitem['quantity'],
        'price': cartitem['price'],
        'menuitem_id': cartitem['menuitem_id'],
        'menuitem': cartitem['menuitem']
    } for cartitem in cartitem_list]

    return jsonify(result)