# models/menuitem.py

from .db import db

# Define the MenuItem model
class MenuItem(db.Model):
    __tablename__ = 'menuitem'
    # proprietary fields
    id = db.Column(db.Integer, primary_key=True)
    imagePath = db.Column(db.String(255))
    title = db.Column(db.String(255))
    price = db.Column(db.Float)
    category = db.Column(db.String(255))
    description = db.Column(db.Text)
    available = db.Column(db.Boolean)
    # Define any relationships here if necessary
    # For example, if MenuItem has a one-to-many relationship with UserReview, you can define it as:
    #user_reviews = db.relationship('UserReview', backref='menu_item', lazy=True)