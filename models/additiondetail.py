# models/additiondetail.py

from .db import db

class AdditionDetail(db.Model):
    __tablename__ = 'additiondetail'

    # Proprietary fields 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    price = db.Column(db.Float)
    addition_id = db.Column(db.Integer, db.ForeignKey('addition.id'))

    def __repr__(self):
        return f"<AdditionDetail {self.id}>"