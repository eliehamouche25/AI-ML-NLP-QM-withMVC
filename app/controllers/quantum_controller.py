from flask import Blueprint, render_template, request, redirect, url_for
from app.models.quantum_model import QuantumExperiment, db

quantum_bp = Blueprint('quantum', __name__)

@quantum_bp.route('/quantum')
def index():
    experiments = QuantumExperiment.query.all()
    return render_template('quantum/index.html', experiments=experiments)

@quantum_bp.route('/quantum/add', methods=['GET', 'POST'])
def add_experiment():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        new_experiment = QuantumExperiment(name=name, description=description)
        db.session.add(new_experiment)
        db.session.commit()
        return redirect(url_for('quantum.index'))
    return render_template('quantum/add.html')