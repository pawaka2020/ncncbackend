# routes/portal/dashboard/page.py

from flask import Blueprint, render_template, request, redirect, url_for
from blueprints import portal_bp

# S 
@portal_bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard_page():
    return render_template('dashboard/page.html')

# User will see:
# orders created by all users : current, completed and canceled.
# 