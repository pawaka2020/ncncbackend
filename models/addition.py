from .db import db
from .additiondetail import AdditionDetail

class Addition(db.Model):
    __tablename__ = 'addition'
    # Proprietary fields
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    selectedprice = db.Column(db.Float)
    selectedindex = db.Column(db.Integer)
    menuitem_id = db.Column(db.Integer, db.ForeignKey('menuitem.id'))
    # To-many relationships
    addition_details = db.relationship('AdditionDetail', backref='addition', lazy=True)

    def __repr__(self):
        return f"<Addition {self.id}>"