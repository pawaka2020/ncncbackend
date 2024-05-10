# routes/dashboard/page.py

from flask import Blueprint, render_template, request, redirect, url_for
from blueprints import portal_bp

# Define a dictionary to store dummy user credentials
dummy_user = {'username': 'username', 'password': 'password'}

@portal_bp.route('/dashboard', methods=['GET', 'POST'])
def dashboard_page():
    error = None  # Initialize error message variable

    if request.method == 'POST':
        # Get the submitted username and password from the form
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Check if username and password are not empty
        if not username or not password:
            error = 'Error: Username and password are required.'
        else:
            # Check if the submitted credentials match the dummy user credentials
            if username == dummy_user['username'] and password == dummy_user['password']:
                # If the credentials match, consider the user logged in
                # Redirect the user to the dashboard page
                return redirect(url_for('portal_bp.dashboard'))
            else:
                # If the credentials do not match, set an error message
                error = 'Error: Incorrect login info. Please try again.'

    # Render the dashboard page template with error message
    return render_template('dashboard/page.html', error=error)
