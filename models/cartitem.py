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
    #menuitem_id = db.Column(db.Integer)
    price = db.Column(db.Float)

    # Relationships with classes below it. (IGNORE THIS for now)
    menuitem = db.relationship('MenuItem', backref='cart_item', lazy=True, foreign_keys=[menuitem_id])

    # Relationships with classes above it
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # def from_json(data):
    #     if data:
    #         return CartItem(
    #             price=data.get('price'),
    #             quantity=data.get('quantity'),
    #             # menuitem = get_menuitem(data.get('menuitem'))
    #         )
    #     return None


    # def from_json(data):
    #     if data:
    #         price = data.get('price')
    #         quantity = data.get('quantity')
    #         menuitems_data = data.get('menuitem')
    #         if menuitems_data:
    #             menuitems = [MenuItem(title=item.get('title')) for item in menuitems_data]
    #             return CartItem(
    #                 price=price,
    #                 quantity=quantity,
    #                 menuitem=menuitems
    #             )
    #     else:
    #         return CartItem(
    #                 price=price,
    #                 quantity=quantity
    #         )
    #     return None
    


    def from_json(data):
        if data:
            return CartItem(
                # proprietary fields
                price=data.get('price'),
                quantity=data.get('quantity'),
                # objects linked beneath it
                # menuitem=list_from_json(data.get('menuitem')),
                menuitem = MenuItem.list_from_json(data.get('menuitem'))
        )
        return None

def list_from_json(data):
    if data: 
        menu_items = []
        for item_data in data:
            title = item_data.get('title')
            menu_item = MenuItem(title=title)
            menu_items.append(menu_item)
        return menu_items
    return None

#
#     [
#   {
#     "content": null,
#     "id": 88,
#     "menuitem_id": null,
#     "price": 10.0,
#     "quantity": 1,
#     "user_id": 71
#     "menuitem" : [
#       {
#         "title" : "Coffee"    
#       }
#      ]
#    }
# ]















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
            # 'user': {
            #     'id': self.user.id,
            #     'name': self.user.name,
            #     'email': self.user.email
            #     # Add more attributes from User if needed
            # }
        }