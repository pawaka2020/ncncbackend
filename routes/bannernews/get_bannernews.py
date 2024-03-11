# routes/bannernews/get_bannernews.py

from flask import Blueprint, jsonify, send_from_directory
from models.bannernews import BannerNews

get_bannernews_bp = Blueprint('get_bannernews_bp', __name__)

@get_bannernews_bp.route('/get_bannernews', methods=['GET'])
def get_bannernews():
    bannernews = BannerNews.query.all()
    bannernews_list = [{'id': news.id, 'image': news.image, 'article': news.article} for news in bannernews]
    return jsonify(bannernews_list)

@get_bannernews_bp.route('/static/images/bannernews/<path:filename>')
def serve_banner_image(filename):
    return send_from_directory('static/images/bannernews/', filename)