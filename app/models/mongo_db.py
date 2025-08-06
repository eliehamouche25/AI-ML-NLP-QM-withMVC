
from pymongo import MongoClient

def get_qm_data():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["quantumDB"]
    collection = db["quantumParticles"]
    return list(collection.find())


 