# routes/portal/main/page.py

from flask import Blueprint, render_template, request, jsonify
from blueprints import portal_bp

@portal_bp.route('/')
def main_page():
    return render_template('main/page.html', content='NCNC backend')

@portal_bp.route('/login_portal_user', methods=['POST'])
def login_portal_user():
    print('hghjgjhgjh ')
    return jsonify({"error": "TODO"}), 401