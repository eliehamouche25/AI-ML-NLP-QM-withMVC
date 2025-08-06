
from flask import Blueprint, request, jsonify
from app.extensions import mongo

from app.models.user_model import mysql  # If you're using a shared mysql instance
from app.models.quantum_model import mongo  # If you're using a shared mongo instance

zone24_bp = Blueprint('zone24_bp', __name__)

@zone24_bp.route('/quantum/data')
def get_quantum_data():
    particles = mongo.db.quantumParticles.find()
    results = []
    for p in particles:
        p['_id'] = str(p['_id'])  # Convert ObjectId to string
        results.append(p)
    return jsonify(results)


@zone24_bp.route('/users')
def get_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT id, username FROM users")
    rows = cur.fetchall()
    cur.close()
    # Optional: convert to list of dicts
    users = [{"id": row[0], "username": row[1]} for row in rows]
    return jsonify(users)


@zone24_bp.route('/search')
def search():
    query = request.args.get('q', '').lower()

    # EXAMPLE: Replace with your MongoDB logic
    dummy_data = ["Artificial Intelligence", "Machine Learning", "Quantum Computing", "Natural Language Processing"]
    results = [item for item in dummy_data if query in item.lower()]

    return jsonify({'results': results})