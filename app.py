from flask import Flask
from models.db import db
# routes
# countries
#from routes.country.get_countries import get_countries_bp
# fullnews
#from routes.fullnews.get_fullnews import get_fullnews_bp
#from routes.fullnews_routes import fullnews_bp
# bannernews
#from routes.bannernews.get_bannernews import get_bannernews_bp
#from routes.bannernews_routes import bannernews_bp
# menuitem
#from routes.menuitem_routes import menuitem_bp
#from routes.menuitem.get_menuitems import get_menuitems_bp
#from routes.verify_routes import verify_bp 
#from routes.verify_code_routes import verify_code_bp
#from routes.verify_email_routes import verify_email_bp
#from routes.verify_email_code_routes import verify_email_code_bp
#from routes.cartitem_routes import cartitem_bp
#from routes.cartitem.get_cartitems import get_cartitems
# user
#from routes.user.get_users import get_users_bp
#from routes.user.update_user import update_user_bp
#utils
from utils.send_email import send_email
#from models.user import find_registered_user
#
from flask import Flask
from flask_mail import Mail, Message
#

from routes.user.add_cart_user import add_cart_user
from routes.user.edit_cart_user import edit_cart_user
from routes.user.delete_cart_user import delete_cart_user
#
# Blueprints
from blueprints import country_bp
from blueprints import fullnews_bp
from blueprints import bannernews_bp
from blueprints import menuitem_bp
#from blueprints import user_bp
from blueprints import users_bp
from blueprints import cartitem_bp
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

app = Flask(__name__)

# postgreSQL. I will disable this later
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ylteicz@localhost/mydatabase'
db.init_app(app)

# Register blueprints
# country
# app.register_blueprint(get_countries_bp)
# fullnews
# app.register_blueprint(fullnews_bp)
#app.register_blueprint(get_fullnews_bp)
# bannernews
# app.register_blueprint(bannernews_bp)
#app.register_blueprint(get_bannernews_bp)
# menuitem
# app.register_blueprint(menuitem_bp)
#app.register_blueprint(get_menuitems_bp)
# cartitem
#app.register_blueprint(get_cartitem_bp)
# app.register_blueprint(verify_bp)
# app.register_blueprint(verify_code_bp)
#app.register_blueprint(verify_email_bp)
#app.register_blueprint(verify_email_code_bp)
# user
#app.register_blueprint(get_users_bp)
#app.register_blueprint(update_user_bp)
#app.register_blueprint(user_bp)
##### blueprint (MONGODB)
# country
app.register_blueprint(country_bp)
app.register_blueprint(fullnews_bp)
app.register_blueprint(bannernews_bp)
app.register_blueprint(menuitem_bp)
app.register_blueprint(users_bp)
app.register_blueprint(cartitem_bp)


# cartitem 
#app.register_blueprint(cartitem_bp)

@app.route('/')
def hello_world():
    return 'NCNC backend'

if __name__ == '__main__':
    with app.app_context():  
        # Use this space to test your functions
        print("")
    app.run(host='192.168.1.21', debug=True)