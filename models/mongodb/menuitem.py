# models/mongodb/menuitem.py

from .db import db

class MenuItem:
    def __init__(self, id, title, description, category, price, imagepath, available, additions, ingredients, userreviews):
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.price = price
        self.imagepath = imagepath
        self.available = available
        self.additions = additions
        self.ingredients = ingredients
        self.userreviews = userreviews

    def save(self):
        db.menuitems.insert_one({
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'price': self.price,
            'imagepath': self.imagepath,
            'available': self.available,
            'additions': self.additions,
            'ingredients': self.ingredients,
            'userreviews': self.userreviews
        })
