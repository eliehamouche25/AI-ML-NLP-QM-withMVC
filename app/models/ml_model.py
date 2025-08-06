from app.extensions import db

class MLModel(db.Model):

    __tablename__ = 'ml_models'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    accuracy = db.Column(db.Float)

    def __repr__(self):
        return f"<MLModel {self.name}>"
    

   