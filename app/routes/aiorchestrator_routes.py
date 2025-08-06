 
from flask import Blueprint, render_template
from flask_login import login_required

# Define the Blueprints here (no re-imports)
aiorchestrator_bp = Blueprint('aiorchestrator', __name__)
ai_bp = Blueprint('ai', __name__)

@ai_bp.route('/ml')
@login_required
def ml_module():
    return render_template('ml.html')

@ai_bp.route('/nlp')
@login_required
def nlp_module():
    return render_template('nlp.html')

def register_routes(app):
    # Register all blueprints needed here
    app.register_blueprint(ai_bp, url_prefix='/ai')
    app.register_blueprint(aiorchestrator_bp, url_prefix='/aiorchestrator')




 