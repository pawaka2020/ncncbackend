# routes/menuitem_routes.py

from flask import Blueprint, jsonify, send_from_directory
from models.menuitem import MenuItem

menuitem_bp = Blueprint('menuitem_bp', __name__)

@menuitem_bp.route('/menuitems', methods=['GET'])
def get_menuitems():
    menuitems = MenuItem.query.all()
    menuitem_list = [{'id': item.id, 'title': item.title, 'price': item.price, 'category': item.category} for item in menuitems]
    return jsonify(menuitem_list)

@menuitem_bp.route('/images/menuitem/<path:filename>')
def serve_menuitem_image(filename):
    return send_from_directory('models/menuitem/', filename)
