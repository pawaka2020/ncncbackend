# blueprints.py

from flask import Blueprint

# Blueprints for MongoDB-based model classes
users_bp = Blueprint('users_bp', __name__)
fullnews_bp = Blueprint('fullnews_bp', __name__)
bannernews_bp = Blueprint('bannernews_bp', __name__)
menuitem_bp = Blueprint('menuitem_bp', __name__)
cartitem_bp = Blueprint('cartitem_bp', __name__)
order_bp = Blueprint("order_bp", __name__)
voucher_bp = Blueprint("voucher_bp", __name__)

# Blueprints for portal web pages
main_bp = Blueprint("main_bp", __name__)
portal_bp = Blueprint("portal_bp", __name__)
