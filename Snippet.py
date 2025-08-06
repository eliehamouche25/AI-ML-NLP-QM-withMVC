from app import create_app
from app.models.user_model import db, User

app = create_app()
with app.app_context():
    db.create_all()
    user = User(username='admin')
    user.set_password('admin123')
    db.session.add(user)
    db.session.commit()
