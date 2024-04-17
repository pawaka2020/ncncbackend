# routes/order/add_order.py
from flask import Flask, Blueprint, jsonify, request
from models.mongodb.db import db
# from models.mongodb.order import Order
from blueprints import order_bp

# Adds an Order object to an existing entry in 'orders' collection
@order_bp.route('/add_order', methods=['POST'])
def add_order():
    json = request.json

    user = db.users.find_one({'user_id': json.get('user_id')})
    print("user id  in add_order = ", json.get('user_id'))

    if user:
        #append with every field of Order class
        user['orders'].append({
            'orderId': json['orderId'],
            'eta': json['eta'],
            'orderPlaced': json['orderPlaced'],
            'status': json['status'],
            'locationLongitude': json['locationLongitude'],
            'locationLatitude': json['locationLatitude'],
            'deliveryAddress': json['deliveryAddress'],
            'phoneNumber': json['phoneNumber'],
            'specialRequest': json['specialRequest'],
            'packageString': json['packageString'],
            'paymentMethod': json['paymentMethod'],
            'onSitePickup': json['onSitePickup'],
            'amount': json['amount'],
            'sst': json['sst'],
            'voucherDeduction': json['voucherDeduction'],
            'subtotal': json['subtotal'],
            'deliveryFee': json['deliveryFee'],
            'roundingAdjustment': json['roundingAdjustment'],
            'appWalletDiscount': json['appWalletDiscount'],
            'totalPrice': json['totalPrice'],
            'active': json['active'],
            # child objects
            'cartItems': json['cartItems'],
            'vouchers': json['vouchers'],
        })
        # cart item emptying    
        user['cart_items'] = []
        # Update the user in the collection
        user['vouchers'] = []
        user['vouchers'] = json['user_vouchers']

        db.users.update_one({'user_id': json.get('user_id')}, {'$set': user})
        return jsonify({'message': 'Order added successfully'}), 200
    else:
        print("Error: User id does not match JSON")
        return jsonify({'message': 'User not found'}), 404