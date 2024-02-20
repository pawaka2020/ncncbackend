from .db import db

# Define the BannerNews model
class BannerNews(db.Model):
    __tablename__ = 'bannernews'
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(255))
    article = db.Column(db.String(255))