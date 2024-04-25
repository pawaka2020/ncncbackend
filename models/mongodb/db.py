# models/mongodb/db.py

# Connection to MongoDB database. 
# Every MongoDB model must use this 'db' value.

from pymongo import MongoClient

MONGODB_HOST = 'mongodb://localhost:27017/'
client = MongoClient(MONGODB_HOST)
db = client['ncncdatabase']
