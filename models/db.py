# models/db.py
# import redis
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()
# redis_client = redis.Redis(host='localhost', port=6379, db=0)