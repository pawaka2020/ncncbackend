from config import IPV4_ADDRESS
#utils
from utils.send_email import send_email
#from models.user import find_registered_user
from flask import Flask
from flask_mail import Mail, Message
# Blueprints
from blueprints import country_bp
from blueprints import fullnews_bp
from blueprints import bannernews_bp
from blueprints import menuitem_bp
# from blueprints import user_bp
from blueprints import users_bp
from blueprints import cartitem_bp
from blueprints import order_bp
from blueprints import voucher_bp
# Routes
from routes.country.get_countries import get_countries
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

app = Flask(__name__)

# postgreSQL. I will disable this later
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ylteicz@localhost/mydatabase'

# country
app.register_blueprint(country_bp)
app.register_blueprint(fullnews_bp)
app.register_blueprint(bannernews_bp)
app.register_blueprint(menuitem_bp)
app.register_blueprint(users_bp)
app.register_blueprint(cartitem_bp)
app.register_blueprint(order_bp)
app.register_blueprint(voucher_bp)

# http://192.168.1.40:5000

@app.route('/')
def hello_world():
    return 'NCNC backend'

if __name__ == '__main__':
    with app.app_context():  
        # Use this space to test your functions
        print("")
    app.run(host=IPV4_ADDRESS, debug=True)