from app import db
from flask_pymongo import PyMongo
from app.extensions import mongo

mongo = PyMongo()

class QuantumModel:
    def __init__(self, db):
        self.db = db
