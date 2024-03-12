from flask import Flask
from models.db import db
# routes
# countries
from routes.country.get_countries import get_countries_bp
# fullnews
from routes.fullnews.get_fullnews import get_fullnews_bp
#from routes.fullnews_routes import fullnews_bp
# bannernews
from routes.bannernews.get_bannernews import get_bannernews_bp
#from routes.bannernews_routes import bannernews_bp
# menuitem
#from routes.menuitem_routes import menuitem_bp
from routes.menuitem.get_menuitems import get_menuitems_bp
#from routes.verify_routes import verify_bp 
#from routes.verify_code_routes import verify_code_bp
from routes.verify_email_routes import verify_email_bp
from routes.verify_email_code_routes import verify_email_code_bp
#from routes.cartitem_routes import cartitem_bp
from routes.cartitem.get_cartitem import get_cartitem_bp
# user
from routes.user.get_users import get_users_bp
from routes.user.update_user import update_user_bp
#utils
from utils.send_email import send_email
#from models.user import find_registered_user
#
from flask import Flask
from flask_mail import Mail, Message

 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ylteicz@localhost/mydatabase'
db.init_app(app)

# Register blueprints
# country
app.register_blueprint(get_countries_bp)
# fullnews
#app.register_blueprint(fullnews_bp)
app.register_blueprint(get_fullnews_bp)
# bannernews
#app.register_blueprint(bannernews_bp)
app.register_blueprint(get_bannernews_bp)
# menuitem
#app.register_blueprint(menuitem_bp)
app.register_blueprint(get_menuitems_bp)
# cartitem
app.register_blueprint(get_cartitem_bp)
#app.register_blueprint(verify_bp)
#app.register_blueprint(verify_code_bp)
app.register_blueprint(verify_email_bp)
app.register_blueprint(verify_email_code_bp)
# user
app.register_blueprint(get_users_bp)
app.register_blueprint(update_user_bp)

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