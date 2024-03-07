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
    # This gives me 'AmbiguousForeignKeysError' error
    menuitem = db.relationship('MenuItem', backref='cart_item', lazy=True, foreign_keys=[menuitem_id])

    # Relationships with classes above it
    #user = db.Column(db.Integer, db.ForeignKey('users.id'))

    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'quantity': self.quantity,
            'price': self.price,
            'menuitem': {
                'id': self.menuitem.id,
                'imagepath': self.menuitem.imagepath,
                'title': self.menuitem.title,
                'price': self.menuitem.price,
                'category': self.menuitem.category,
                'description': self.menuitem.description,
                'available': self.menuitem.available
                # Add more attributes from MenuItem if needed
            },
            'user': {
                'id': self.user.id,
                'name': self.user.name,
                'email': self.user.email
                # Add more attributes from User if needed
            }
        }