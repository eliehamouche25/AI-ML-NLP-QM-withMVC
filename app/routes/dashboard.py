 
from flask import Blueprint, render_template, session, redirect, url_for

dashboard_bp = Blueprint('dashboard', __name__)



@dashboard_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')