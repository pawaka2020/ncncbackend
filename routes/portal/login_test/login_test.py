# routes/portal/login_test.py

from flask import Blueprint, render_template, request, make_response, redirect, url_for, jsonify
from blueprints import portal_bp
from flask_login import login_user, logout_user, login_required, current_user

@portal_bp.route('/login_test')
def login_page_test():
    return render_template('login_test.html')

def check_authorization():
    auth_cookie = request.cookies.get('auth_cookie')
    if not auth_cookie or auth_cookie != 'expected_cookie_value':
        return "Error 401: Unauthorized access", 401
    return None

def custom_decorator(func):
    def decorated_function(*args, **kwargs):
        print("custom decorator activated")
        return func(*args, **kwargs)
    return decorated_function

@portal_bp.route('/dashboard_page_test')
def dashboard_page_test():
    auth_error = False
    auth_error = check_authorization()
    if auth_error:
        return auth_error
    return "This is the dashboard"

def sanitize(username, password):
    sanitized_username = username.strip().lower()  # Remove leading/trailing whitespace and convert to lowercase
    sanitized_password = password.strip()  # Remove leading/trailing whitespace
    return sanitized_username, sanitized_password

@portal_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data:
        return jsonify({"error": "Invalid request. JSON data required."}), 400

    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"error": "Username and password are required fields."}), 400

    print("username =", username)
    print("password =", password)

    username, password = sanitize(username, password)

    # placeholder return response, I will change later.
    return jsonify({"message": "Login successful."}), 200
