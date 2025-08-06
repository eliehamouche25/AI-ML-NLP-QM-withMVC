from flask import Blueprint, render_template, request, redirect, url_for
from app.models.ml_model import MLModel
from app import db

ml_bp = Blueprint('ml', __name__)
 


@ml_bp.route('/ml')
def show_ml_models():
    models = MLModel.query.all()
    return render_template('ml_list.html', models=models)

@ml_bp.route('/ml/create', methods=['POST'])
def create_ml_model():
    name = request.form['name']
    accuracy = float(request.form['accuracy'])
    new_model = MLModel(name=name, accuracy=accuracy)
    db.session.add(new_model)
    db.session.commit()
    return redirect(url_for('ml.show_ml_models'))

 
@ml_bp.route('/ml')
def ml():
    return render_template('ml.html')
