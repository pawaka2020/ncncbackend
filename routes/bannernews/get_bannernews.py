# routes/bannernews/get_bannernews.py

from flask import Flask, Blueprint, jsonify, send_from_directory
from models.mongodb.db import db
from models.mongodb.bannernews import BannerNews
from blueprints import bannernews_bp

# Displays all objects of BannerNews in JSON format on the browser
@bannernews_bp.route('/get_bannernews', methods=['GET'])
def get_bannernews():
    bannernews_list = list(db['bannernews'].find({}))

    result = [{
        'article' : bannernews['article'],
        'image' : bannernews['image'],
    } for bannernews in bannernews_list]

    return jsonify(result)

@bannernews_bp.route('/static/images/bannernews/<path:filename>')
def serve_banner_image(filename):
    return send_from_directory('static/images/bannernews/', filename)