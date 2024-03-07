# models/fullnews.py

from .db import db

# Define the FullNews model
class FullNews(db.Model):
    __tablename__ = 'fullnews'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
