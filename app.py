from flask import Flask
from models.db import db
# routes
from routes.country_routes import country_bp
from routes.fullnews_routes import fullnews_bp
from routes.bannernews_routes import bannernews_bp
from routes.menuitem_routes import menuitem_bp
from routes.verify_routes import verify_bp 
from routes.verify_code_routes import verify_code_bp
from routes.user_routes import user_bp
from models.user import find_registered_user
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ylteicz@localhost/mydatabase'
db.init_app(app)

# Register blueprints
app.register_blueprint(country_bp)
app.register_blueprint(fullnews_bp)
app.register_blueprint(bannernews_bp)
app.register_blueprint(menuitem_bp)
app.register_blueprint(verify_bp)  # Register the verify blueprint
app.register_blueprint(verify_code_bp)
app.register_blueprint(user_bp)

@app.route('/')
def hello_world():
    return 'NCNC backend'

if __name__ == '__main__':
    with app.app_context():  
        # Use this space to test your functions
        user = find_registered_user('+1234567890')
        if (user):
            print("on main, user found")
        else:
            print('on main, user not found')
    app.run(host='192.168.1.21', debug=True)