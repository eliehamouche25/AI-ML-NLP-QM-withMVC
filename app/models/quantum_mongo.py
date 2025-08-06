from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
mongo_db = client["quantum_ai_db"]
quantum_collection = mongo_db["quantum_quality_data"]

def insert_quantum_data(data):
    quantum_collection.insert_one(data)

def get_all_quantum_data():
    return list(quantum_collection.find())