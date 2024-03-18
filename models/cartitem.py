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
    def __from_json(data):
        menuitems_data = data.get('menuitem')
        menuitems = [
            MenuItem(
                title=item.get('title'),
                imagepath=item.get('imagepath')
            )   for item in menuitems_data
        ]
        return menuitems

    @staticmethod
    def from_json(data):
        if data:
            menuitem_data = data.get('menuitem')

        # Create a list to hold MenuItem objects
            menuitems = []

        # Create MenuItem objects and add them to the session
            if menuitem_data:
                for item_data in menuitem_data:
                    menuitem = MenuItem(
                        imagepath=item_data.get('imagepath'),
                        title=item_data.get('title')
                )
                menuitems.append(menuitem)
            print("menu title = ", menuitems[0].title)
        
            # Create CartItem object
            cartitem = CartItem(
                id=data.get('id'),
                price=data.get('price'),
                quantity=data.get('quantity'),
               
                #menuitem=menuitems  # Associate MenuItem objects with CartItem
            )
            if cartitem.menuitem is None:
                cartitem.menuitem = []
            # Associate CartItem with MenuItem objects
            #cartitem.menuitem = menuitems
            #cartitem.menuitem.append(CartItem(title = 'asdsad'))
                        # Associate CartItem with MenuItem objects
            cartitem.menuitem.extend(MenuItem())
        return None

    @staticmethod
    def list_from_json2(menuitems_data):
        #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        menuitems = []
        if menuitems_data:

            for menuitem_data in menuitems_data:
                print("title = ", menuitem_data.get('title'))
                menuitem = MenuItem(
                    imagepath=menuitem_data.get('image_path'),
                    title=menuitem_data.get('title')
                    # Add other fields if necessary
                )
                menuitems.append(menuitem)
        return menuitems




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