# routes/order/delete_order.py

from flask import Flask, Blueprint, jsonify, request
from models.mongodb.db import db
# from models.mongodb.order import Order
from blueprints import order_bp

# Adds an Order object to an existing entry in 'orders' collection
@order_bp.route('/delete_order', methods=['POST'])
def delete_order():
    json_data = request.json

    user_id = json_data.get('user_id')
    order_id = json_data.get('order_id')

    if not user_id or not order_id:
        return jsonify({'error': 'Invalid request data'}), 400
    
    # Find user in 'users' collection using matching 'user_id'
    user = db.users.find_one({'user_id': user_id})

    #'orders': [],
    #'orderId'
    if user:
        orders = user.get('orders', [])
        for order in orders:
            if order.get('orderId') == order_id:
                orders.remove(order)
                break

        db.users.update_one({'user_id': user_id}, {'$set': {'orders': orders}})
        return jsonify({'message': 'Order deleted successfully'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404