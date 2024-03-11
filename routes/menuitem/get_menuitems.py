# routes/menuitem/get_menuitems.py

from flask import Blueprint, jsonify, send_from_directory
from models.menuitem import MenuItem

get_menuitems_bp = Blueprint('get_menuitems_bp', __name__)

@get_menuitems_bp.route('/get_menuitems', methods=['GET'])
def get_menuitems():
    menuitems = MenuItem.query.all()
    menuitem_list = []
    for item in menuitems:
        # Extract user reviews
        user_reviews = [{
            'name': review.name, 
            'message': review.message, 
            'stars': review.stars
        } for review in item.userreview]
        # Extract additions
        additions = []
        for addition in item.addition:
            addition_dict = {
                'title': addition.title,
                'selectedPrice': addition.selectedprice,
                'selectedIndex': addition.selectedindex,
                'addition_details': [{
                    'name': detail.name,
                    'price': detail.price
                } for detail in addition.addition_details]  # Extract addition details
            }
            additions.append(addition_dict)
        # Extract ingredients
        ingredients = [{
            'name': ingredient.name
        } for ingredient in item.ingredient]
        menuitem_dict = {
            'id': item.id,
            'imagepath': item.imagepath,
            'title': item.title,
            'price': item.price,
            'description': item.description,
            'category': item.category,
            'available': item.available,
            'userreviews': [{
                'name': review.name, 
                'message': review.message, 
                'stars': review.stars
            } for review in item.userreview],
            'additions': additions,
            'ingredients': ingredients,
            'cartitems' : item.cartitem_id,
        }
        menuitem_list.append(menuitem_dict)
    return jsonify(menuitem_list)

@get_menuitems_bp.route('/static/images/menuitem/<path:filename>')
def serve_menuitem_image(filename):
    return send_from_directory('static/images/menuitem/', filename)