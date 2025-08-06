from flask import Blueprint, render_template, request
import mysql.connector
 


main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def homepage():
    return render_template('index.html')  # 👈 ta vraie page d'accueil

@main_bp.route('/option/<name>')
def load_option(name):
    if name == "AI":
        data = get_ai_data()
        return render_template('partials/ai_data.html', data=data)
    elif name == "QM":
        data = get_qm_data()
        return render_template('partials/qm_data.html', data=data)
    else:
        return f'<p><strong>{name}</strong> section loaded in Zone 4.</p>'

@main_bp.route('/search')
def search():
    query = request.args.get('q', '').lower()

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='elie',
        database='myprojectdb'
    )

    cursor = connection.cursor()
    cursor.execute("SELECT title FROM articles WHERE LOWER(title) LIKE %s", ('%' + query + '%',))
    results = cursor.fetchall()
    connection.close()

    if not results:
        return '<p>No results found.</p>'

    html = '<ul>'
    for row in results:
        html += f'<li>{row[0]}</li>'
    html += '</ul>'

    return html

 

def get_ai_data():
    # Example: this could be a DB query or API call
    return {
        "title": "Artificial Intelligence Overview",
        "content": "AI is the simulation of human intelligence in machines."
    }

def get_qm_data():
    # Example: this could be a DB query or API call
    return {
        "title": "Quantum Mechanics Basics",
        "content": "Quantum Mechanics studies the behavior of particles at atomic scales."
    }