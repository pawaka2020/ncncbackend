#routes/fullnews/get_fullnews.py

# from flask import Blueprint, jsonify, send_from_directory
# from models.fullnews import FullNews

# get_fullnews_bp = Blueprint('get_fullnews_bp', __name__)

# @get_fullnews_bp.route('/get_fullnews', methods=['GET'])
# def get_fullnews():
#     fullnews = FullNews.query.all()
#     fullnews_list = [{'id': news.id, 'name': news.name} for news in fullnews]
#     return jsonify(fullnews_list)

# @get_fullnews_bp.route('/static/images/fullnews/<path:filename>')
# def serve_fullnews_image(filename):
#     return send_from_directory('static/images/fullnews/', filename)

from flask import Flask, Blueprint, jsonify, send_from_directory
from models.mongodb.db import db
from models.mongodb.fullnews import FullNews
from blueprints import fullnews_bp

# Displays all objects of FullNews in JSON format on the browser
@fullnews_bp.route('/get_fullnews', methods=['GET'])
def get_fullnews():
    fullnews_list = list(db['fullnews'].find({}))

    result = [{
        'name' : fullnews['name'],
        } for fullnews in fullnews_list]

    return jsonify(result)

@fullnews_bp.route('/static/images/fullnews/<path:filename>')
def serve_fullnews_image(filename):
    return send_from_directory('static/images/fullnews/', filename)