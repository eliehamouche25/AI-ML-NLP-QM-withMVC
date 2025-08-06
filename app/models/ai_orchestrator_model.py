# app/models/ai_orchestrator_model.py
from app.extensions import db

class AIOrchestrator(db.Model):
    __tablename__ = 'ai_orchestrators'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
