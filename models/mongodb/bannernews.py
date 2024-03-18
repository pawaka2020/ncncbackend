# models/mongodb/bannernews.py

from .db import db

class BannerNews:
    # Constructor and field definition
    def __init__(self, article, image):
        self.article = article
        self.image = image

    def save(self):
        db.bannernews.insert_one({
            'article': self.article,
            'image' : self.image,
        })