from flask import Blueprint, render_template, request, redirect, url_for

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    return render_template('auth/login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            return "Passwords do not match", 400
        # TODO: Enregistrer l'utilisateur en base de données ici
        return redirect(url_for('auth.login'))
    # GET request → affiche le formulaire
    return render_template('auth/register.html')


@auth_bp.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    # TODO: authentification (logique à implémenter)
    return redirect(url_for('main.index'))