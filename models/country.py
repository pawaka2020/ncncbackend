# models/country.py

from .db import db

# Define the Country model
class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
            # Add more fields as needed
        }