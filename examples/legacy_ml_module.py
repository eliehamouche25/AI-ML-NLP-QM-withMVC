from flask import Blueprint, request, render_template, redirect, url_for
from app.models.ml_model import MLModel
from app import db

ml_bp = Blueprint('ml', __name__, url_prefix='/ml')

@ml_bp.route('/')
def ml_list():
    ml_objects = MLModel.query.all()
    return render_template('ml_list.html', ml_objects=ml_objects)

@ml_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_ml(id):
    ml_object = MLModel.query.get_or_404(id)
    if request.method == 'POST':
        new_status = request.form.get('status')
        ml_object.update_status(new_status)
        db.session.commit()
        return redirect(url_for('ml.ml_list'))
    return render_template('ml_edit.html', ml_object=ml_object)