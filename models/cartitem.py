# models/cartitem.py

from .db import db

class CartItem(db.Model):
    __tablename__ = 'cartitem'

    # Proprietary fields.
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    quantity = db.Column(db.Integer)
    menuitem_id = db.Column(db.Integer, db.ForeignKey('menuitem.id'))
    price = db.Column(db.Float)

    # Relationships with classes below it.
    menuitem = db.relationship('MenuItem', back_populates='cartitems')