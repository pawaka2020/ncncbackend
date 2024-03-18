# routes/menuitem/get_menuitems.py

# from flask import Blueprint, jsonify, send_from_directory
# from models.menuitem import MenuItem

# get_menuitems_bp = Blueprint('get_menuitems_bp', __name__)

# @get_menuitems_bp.route('/get_menuitems', methods=['GET'])
# def get_menuitems():
#     menuitems = MenuItem.query.all()
#     menuitem_list = []
#     for item in menuitems:
#         # Extract user reviews
#         user_reviews = [{
#             'name': review.name, 
#             'message': review.message, 
#             'stars': review.stars
#         } for review in item.userreview]
#         # Extract additions
#         additions = []
#         for addition in item.addition:
#             addition_dict = {
#                 'title': addition.title,
#                 'selectedPrice': addition.selectedprice,
#                 'selectedIndex': addition.selectedindex,
#                 'addition_details': [{
#                     'name': detail.name,
#                     'price': detail.price
#                 } for detail in addition.addition_details]  # Extract addition details
#             }
#             additions.append(addition_dict)
#         # Extract ingredients
#         ingredients = [{
#             'name': ingredient.name
#         } for ingredient in item.ingredient]
#         menuitem_dict = {
#             'id': item.id,
#             'imagepath': item.imagepath,
#             'title': item.title,
#             'price': item.price,
#             'description': item.description,
#             'category': item.category,
#             'available': item.available,
#             'userreviews': [{
#                 'name': review.name, 
#                 'message': review.message, 
#                 'stars': review.stars
#             } for review in item.userreview],
#             'additions': additions,
#             'ingredients': ingredients,
#             'cartitems' : item.cartitem_id,
#         }
#         menuitem_list.append(menuitem_dict)
#     return jsonify(menuitem_list)

# @get_menuitems_bp.route('/static/images/menuitem/<path:filename>')
# def serve_menuitem_image(filename):
#     return send_from_directory('static/images/menuitem/', filename)

# routes/menuitem/get_menuitems.py

from flask import Flask, Blueprint, jsonify, send_from_directory
from models.mongodb.db import db
from models.mongodb.menuitem import MenuItem
from blueprints import menuitem_bp

# Displays all objects of MenuItem in JSON format on the browser
@menuitem_bp.route('/get_menuitems', methods=['GET'])
def get_menuitems():
    menuitems_list = list(db['menuitem'].find({}))

    result = [{
        'id': item['id'],
        'title': item['title'],
        'description': item['description'],
        'category': item['category'],
        'price': item['price'],
        'imagepath': item['imagepath'],
        'available': item['available'],
        'additions': item['additions'],
        'ingredients': item['ingredients'],
        'userreviews': item['userreviews']
    } for item in menuitems_list]

    return jsonify(result)

@menuitem_bp.route('/static/images/menuitem/<path:filename>')
def serve_menuitem_image(filename):
    return send_from_directory('static/images/menuitem/', filename)