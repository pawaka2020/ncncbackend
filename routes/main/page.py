# routes/main/page.py

from flask import Blueprint, render_template
from blueprints import portal_bp

@portal_bp.route('/')
def main_page():
    return render_template('main/page.html', content='NCNC backend')