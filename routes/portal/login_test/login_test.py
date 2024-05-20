# routes/portal/login_test.py

from flask import Blueprint, render_template, request, jsonify
from blueprints import portal_bp
from models.mongodb.db import db
from routes.portal.login_test.hash_password import hash_password
from config import SECRET_KEY
import jwt
from datetime import datetime, timedelta, timezone
from flask import make_response
from functools import wraps
from bson import ObjectId

@portal_bp.route('/login_test')
def login_page_test():
    return render_template('login_test.html')

def get_login_data(request):
    data = request.json
    username = data.get('username')
    password = data.get('password')
    print("username =", username)
    print("password =", password)
    return username, password

def get_registered_user(username):
    user = db['portal_users'].find_one({'username': username}, {'salt': 1, 'hashed_password': 1, '_id':1})
    return user

def match_password(user, password):
    salt = user.get('salt')
    hashed_password = user.get('hashed_password')
    hashed_password_ = hash_password(password, salt)
    print("hashed_password =", hashed_password)
    print("hashed_password_ =", hashed_password_)
    return hashed_password == hashed_password_

# TODO later
def get_token(user):
    secret_key = SECRET_KEY
    user_id = user.get('_id')
    validity_hours = 48

    payload = {
        'user_id': str(user_id),
        'exp': datetime.now(timezone.utc) + timedelta(hours=validity_hours)
        # insert other data as appropriate here.
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token
    #return token.encode('utf-8')

# Stores this token into collection 'portal_user_tokens'
def store_token(username, token):
    token_doc = {
        'username': username,
        'token': token,
        # additional details from user go here if needed.
    }
    db['portal_user_tokens'].insert_one(token_doc)
    print("Token stored successfully.")

def create_cookie(token):
    response = make_response()
    decoded_token = token.decode('utf-8')  # Decode the token bytes to string
    response.set_cookie('login_token', decoded_token, httponly=False, secure=False, samesite='Strict')
    return response

@portal_bp.route('/login', methods=['POST'])
def login():
    token = None
    #cookie = None
    username, password = get_login_data(request)
    if not username or not password:
        return jsonify({"error": "Username and password are required fields."}), 400

    user = get_registered_user(username)
    if not user:
        return jsonify({"error": "User not found."}), 400

    if match_password(user, password):
        token = get_token(user)
        store_token(username, token)
        #cookie = create_cookie(token)
        # return cookie, 200
        return jsonify({"message": "Login successful.", "token": token}), 200
    else:
        return jsonify({"error": "Password incorrect."}), 401

def check_authorization():
    auth_cookie = request.cookies.get('auth_cookie')
    if not auth_cookie or auth_cookie != 'expected_cookie_value':
        return "Error 401: Unauthorized access", 401
    return None

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({"error": "Unauthorized access"}), 401
        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            user_id = data.get('user_id')
            user_id_object = ObjectId(user_id)
            user = db['portal_users'].find_one({'_id': user_id_object})

            if user is None:
                return jsonify({"error": "User not found"}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401
        return f(*args, **kwargs)
    return decorated_function

@portal_bp.route('/dashboard_page_test')
@token_required
def dashboard_page_test():
    return "This is the dashboard"
    
def custom_decorator(func):
    def decorated_function(*args, **kwargs):
        print("custom decorator activated")
        return func(*args, **kwargs)
    return decorated_function