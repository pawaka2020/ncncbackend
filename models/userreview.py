from .db import db

class UserReview(db.Model):
    __tablename__ = 'userreview'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    message = db.Column(db.Text)
    stars = db.Column(db.Integer)
    menuitem_id = db.Column(db.Integer, db.ForeignKey('menuitem.id'))

    def __repr__(self):
        return f'<UserReview {self.id}>'
