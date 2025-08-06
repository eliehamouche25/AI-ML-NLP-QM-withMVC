import os  # ✅ Make sure this is at the top

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:elie@localhost/myprojectdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MONGO_URI = 'mongodb://localhost:27017/quntumDB'
    
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_super_secret_key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # or another valid URI like PostgreSQL or MySQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False