# routes/portal/login_test.py

from flask import Blueprint, render_template, request, jsonify
from blueprints import portal_bp
from models.mongodb.db import db
from routes.portal.login_test.hash_password import hash_password
from config import SECRET_KEY
import jwt
from datetime import datetime, timedelta, timezone
from flask import make_response

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
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token.encode('utf-8')

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
    decoded_token = token.decode('utf-8')
    response.set_cookie('session_token', decoded_token, httponly=True, secure=True, samesite='Strict')
    return response

@portal_bp.route('/login', methods=['POST'])
def login():
    token = None
    cookie = None
    username, password = get_login_data(request)
    if not username or not password:
        return jsonify({"error": "Username and password are required fields."}), 400

    user = get_registered_user(username)
    if not user:
        return jsonify({"error": "User not found."}), 400

    if match_password(user, password):
        token = get_token(user)
        store_token(username, token)
        response = create_cookie(token)
        return response, 200
    else:
        return jsonify({"error": "Password incorrect."}), 401

def check_authorization():
    auth_cookie = request.cookies.get('auth_cookie')
    if not auth_cookie or auth_cookie != 'expected_cookie_value':
        return "Error 401: Unauthorized access", 401
    return None

@portal_bp.route('/dashboard_page_test')
def dashboard_page_test():
    # auth_error = False
    # auth_error = check_authorization()
    # if auth_error:
    #     return auth_error
    return "This is the dashboard"

def custom_decorator(func):
    def decorated_function(*args, **kwargs):
        print("custom decorator activated")
        return func(*args, **kwargs)
    return decorated_function

