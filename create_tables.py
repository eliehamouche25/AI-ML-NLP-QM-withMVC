
from app import create_app
from app.extensions import db
from app.models.user_model import User  # Adjust path if needed

app = create_app()

with app.app_context():
    db.create_all()
    print("Tables created!")