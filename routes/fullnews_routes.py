# routes/fullnews_routes.py

from flask import Blueprint, jsonify, send_from_directory
from models.fullnews import FullNews

fullnews_bp = Blueprint('fullnews_bp', __name__)

@fullnews_bp.route('/fullnews', methods=['GET'])
def get_fullnews():
    fullnews = FullNews.query.all()
    fullnews_list = [{'id': news.id, 'name': news.name} for news in fullnews]
    return jsonify(fullnews_list)

@fullnews_bp.route('/images/fullnews/<path:filename>')
def serve_fullnews_image(filename):
    return send_from_directory('static/images/fullnews/', filename)