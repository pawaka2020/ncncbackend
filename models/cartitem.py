# models/cartitem.py

from .db import db
from .menuitem import MenuItem
#from .user import User

class CartItem(db.Model):
    __tablename__ = 'cartitem'

    # Proprietary fields.
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))
    quantity = db.Column(db.Integer)
    menuitem_id = db.Column(db.Integer, db.ForeignKey('menuitem.id'))
    price = db.Column(db.Float)

    # Child objects (TODO)
    menuitem = db.relationship('MenuItem', backref='cart_item', lazy=True, foreign_keys=[menuitem_id])

    # Parent objects
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    @staticmethod
    def from_json(data):
        if data:
            return CartItem(
                # Proprietary fields
                id = data.get('id'),
                price=data.get('price'),
                quantity=data.get('quantity'),
                # Child objects
                menuitem=MenuItem.list_from_json(data.get('menuitem'))
        )
        return None

    @staticmethod
    def list_from_json(data):
        # if data:
        #     list = []
        #     for item_data in data :
        #         list.append(CartItem.from_json(item_data))
        #     return list
        if data:
            return [CartItem.from_json(item_data) for item_data in data]
        return None

    def to_json(self):
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
        }