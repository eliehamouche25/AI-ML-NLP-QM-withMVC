
from flask import Blueprint, render_template



home_controller = Blueprint('home_controller', __name__)
home_bp = Blueprint("home_blueprint", __name__)  # Renamed from "home" to "home_blueprint"

@home_controller.route('/home')
def home():
    return render_template('home.html', active_zone='zone1')
 

@home_controller.route('/zone4')
def zone4():
    return render_template('home.html', active_zone='zone4')

@home_controller.route('/app')
def app():
    return render_template('app.html')

@home_bp.route('/')
def index():
    return render_template('index.html')


@home_controller.route('/zone4')
def register_routes(app):
    app.register_blueprint(home_bp)

 
 
  