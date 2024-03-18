# models/mongodb/db.py

# Connection to MongoDB database. 
# Every MongoDB model must use this 'db' value.

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['ncncdatabase']
