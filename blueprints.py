# blueprints.py

from flask import Blueprint

country_bp = Blueprint('country_bp', __name__)
# old one still using postgreSQL
user_bp = Blueprint('user_bp', __name__)
# new one using MongoDB
users_bp = Blueprint('users_bp', __name__)
fullnews_bp = Blueprint('fullnews_bp', __name__)
bannernews_bp = Blueprint('bannernews_bp', __name__)
menuitem_bp = Blueprint('menuitem_bp', __name__)
cartitem_bp = Blueprint('cartitem_bp', __name__)
order_bp = Blueprint("order_bp", __name__)
voucher_bp = Blueprint("voucher_bp", __name__)