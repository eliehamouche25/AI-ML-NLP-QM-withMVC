from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for, current_app
from datetime import timedelta
from controllers.user_controller import UserController

auth_bp = Blueprint('auth', __name__)
dashboard_bp = Blueprint('dashboard', __name__)
user_controller = UserController()

@auth_bp.route('/signin', methods=['POST'])
def signin():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if user_controller.verify_user(username, password):
        session['user_id'] = username
        session['role'] = user_controller.users[username]['role']  # stocker rôle aussi
        session.permanent = True
        current_app.permanent_session_lifetime = timedelta(minutes=15)
        return jsonify({'status': 'ok', 'username': username})
    else:
        return jsonify({'status': 'error', 'message': 'Invalid credentials'})

@dashboard_bp.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        return render_template('dashboard.html', user=session['user_id'], role=session.get('role'))
    return redirect(url_for('auth.signin'))  # attention à l'endpoint ici