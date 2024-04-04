# routes/voucher/get_vouchers.py

from flask import Flask, Blueprint, jsonify, send_from_directory
from models.mongodb.db import db
from models.mongodb.voucher import Voucher
from blueprints import voucher_bp

# Displays all objects of User in JSON format on the browser
@voucher_bp.route('/get_vouchers', methods=['GET'])
def get_vouchers():
    vouchers_list = list(db['vouchers'].find({}))

    result = [{
        'voucher_id': voucher['voucher_id'],
        'image': voucher['image'],
        'priceDiscount': voucher['priceDiscount'],
        'priceDeduct': voucher['priceDeduct'],
        'expiryDate': voucher['expiryDate'],
        'activated': voucher['activated'],
    }   for voucher in vouchers_list]
    return jsonify(result)

@voucher_bp.route('/static/images/voucher/<path:filename>')
def serve_voucher_image(filename):
    return send_from_directory('static/images/voucher/', filename)