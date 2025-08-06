from app import db

class MLModel(db.Model):
    __tablename__ = 'ml_models'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50))
    parameters = db.Column(db.Text)

    def __repr__(self):
        return f"<MLModel {self.name}>"

    def update_status(self, new_status):
        self.status = new_status
        # ajouter commit dans le controller après l'appel
