from flask import Flask
from models.db import db
from routes.country_routes import country_bp
from routes.fullnews_routes import fullnews_bp
from routes.bannernews_routes import bannernews_bp
from routes.menuitem_routes import menuitem_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:ylteicz@localhost/mydatabase'
db.init_app(app)

# Register blueprints
app.register_blueprint(country_bp)
app.register_blueprint(fullnews_bp)
app.register_blueprint(bannernews_bp)
app.register_blueprint(menuitem_bp)

@app.route('/')
def hello_world():
    return 'NCNC backend'

if __name__ == '__main__':
    app.run(host='192.168.1.19', debug=True)
