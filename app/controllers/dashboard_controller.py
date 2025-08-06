 

from flask import Blueprint, render_template, session, redirect, url_for

# Create a blueprint for the dashboard
dashboard_bp = Blueprint('dashboard', __name__)

# Route for the dashboard page
@dashboard_bp.route('/dashboard')
def dashboard():
    # Check if the user is authenticated
    if 'user_id' not in session:
        print("User not in session – redirecting to login")
        return redirect(url_for('auth.login'))

    print(f"User in session: {session.get('user_id')}")
    return render_template('dashboard.html', username=session.get('username', 'User'))