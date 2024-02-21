from .db import db

class Ingredient(db.Model):
    __tablename__ = 'ingredient'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    menuitem_id = db.Column(db.Integer, db.ForeignKey('menuitem.id'))

    def __repr__(self):
        return f"<Ingredient {self.id}>"
