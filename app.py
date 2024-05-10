# app.py
from config import IPV4_ADDRESS

# Library imports
from flask import Flask
from flask_mail import Mail, Message

# Utils (not used yet)
from utils.send_email import send_email

# Blueprints
from blueprints import fullnews_bp
from blueprints import bannernews_bp
from blueprints import menuitem_bp
from blueprints import users_bp
from blueprints import cartitem_bp
from blueprints import order_bp
from blueprints import voucher_bp
from blueprints import main_bp
from blueprints import portal_bp
#from blueprints import webpages_bp

# Routes
from routes.fullnews.get_fullnews import get_fullnews
from routes.bannernews.get_bannernews import get_bannernews
from routes.menuitem.get_menuitems import get_menuitems
from routes.users.get_users import get_users
from routes.users.request_code import request_code
from routes.users.verify_code import verify_code
from routes.users.logoff import logoff
from routes.users.update_user import update_user
from routes.cartitem.get_cartitems import get_cartitems
from routes.cartitem.add_cartitem import add_cartitem
from routes.cartitem.delete_cartitem import delete_cartitem
from routes.cartitem.edit_cartitem import edit_cartitem
from routes.order.add_order import add_order
from routes.order.delete_order import delete_order
from routes.voucher.get_vouchers import get_vouchers
#from routes.portal.frontpage import frontpage
from routes.portal.main import page
from routes.portal.login import page

# Create new MongoDB collections for first-time run.
from models.mongodb.create_collections import create_collections

# Defines this app as a Flask application.
app = Flask(__name__)

# Blueprint registrations to enable usage of route functions defined under each blueprint
app.register_blueprint(fullnews_bp)
app.register_blueprint(bannernews_bp)
app.register_blueprint(menuitem_bp)
app.register_blueprint(users_bp)
app.register_blueprint(cartitem_bp)
app.register_blueprint(order_bp)
app.register_blueprint(voucher_bp)
# portal blueprints
app.register_blueprint(main_bp)
app.register_blueprint(portal_bp)

# Use this space to test your functions
def test_functions():
    print("TODO")

# Main route that launches the backend at IPV4_ADDRESS defined at config.py
# Since we are now building an internal portal web app on top of this backend, this code is no longer used
@app.route('/')
def hello_world():
    return 'NCNC backend'

if __name__ == '__main__':
    with app.app_context():  
        test_functions()
        create_collections()
    app.run(host=IPV4_ADDRESS, debug=True)