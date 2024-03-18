# models/mongodb/countries.py

from .db import db

class Country:
    # Constructor and field definition
    def __init__(self, name, population):
        self.name = name
        self.population = population

    # Writes a 'Country' object to database.
    def save(self):
        db.countries.insert_one({
            'name': self.name,
            'population': self.population
        })