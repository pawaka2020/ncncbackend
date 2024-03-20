# models/mongodb/cartitem.py

from .db import db

class CartItem:
    def __init__(self, quantity, price, menuitem_id, menuitem):
        self.quantity = quantity
        self.price = price
        self.menuitem_id = menuitem_id
        self.menuitem = menuitem
    
    