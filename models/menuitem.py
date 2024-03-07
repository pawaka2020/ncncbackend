# models/menuitem.py

from .db import db
from .userreview import UserReview
from .addition import Addition
from .ingredient import Ingredient

class MenuItem(db.Model):
    __tablename__ = 'menuitem'

    # Proprietary fields
    id = db.Column(db.Integer, primary_key=True)
    imagepath = db.Column(db.String(255))
    title = db.Column(db.String(255))
    price = db.Column(db.Float)
    category = db.Column(db.String(255))
    description = db.Column(db.Text)
    available = db.Column(db.Boolean)

    # Relationships with classes below it
    userreview = db.relationship('UserReview', backref='menu_item', lazy=True)
    addition = db.relationship('Addition', backref='menu_item', lazy=True)
    ingredient = db.relationship('Ingredient', backref='menu_item', lazy=True)

    # Relationships with classes above it.
    cartitem_id = db.Column(db.Integer, db.ForeignKey('cartitem.id'))
    
    def __repr__(self):
        return f"<MenuItem {self.id}>"
