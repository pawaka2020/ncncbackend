# routes/order/delete_order.py

from flask import Flask, Blueprint, jsonify, request
from models.mongodb.db import db
# from models.mongodb.order import Order
from blueprints import order_bp

# Adds an Order object to an existing entry in 'orders' collection
@order_bp.route('/delete_order', methods=['POST'])
def delete_order():
    print("TODO")