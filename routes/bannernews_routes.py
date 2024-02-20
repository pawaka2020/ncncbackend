# routes/bannernews_routes.py

from flask import Blueprint, jsonify, send_from_directory
from models.bannernews import BannerNews

bannernews_bp = Blueprint('bannernews_bp', __name__)

@bannernews_bp.route('/bannernews', methods=['GET'])
def get_bannernews():
    bannernews = BannerNews.query.all()
    bannernews_list = [{'id': news.id, 'image': news.image, 'article': news.article} for news in bannernews]
    return jsonify(bannernews_list)

@bannernews_bp.route('/images/bannernews/<path:filename>')
def serve_banner_image(filename):
    return send_from_directory('models/bannernews/', filename)
