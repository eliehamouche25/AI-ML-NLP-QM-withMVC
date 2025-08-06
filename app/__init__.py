from flask import Flask
from datetime import timedelta

def create_app():
    app = Flask(__name__)

    from app.routes.main import main_bp
    from app.routes.auth_routes import auth_bp
    from app.routes.dashboard import dashboard_bp  # if you have this

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')  # optional

    return app
 