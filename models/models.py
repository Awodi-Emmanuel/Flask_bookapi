from tkinter.tix import COLUMN
from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    author = db.Column(db.String())
    published = db.Column(db.Sring())
    
    def __init__(self, name, author, published):
        self.name = name
        self.author = author
        self.published = published
        
        
    def __repr__(self):
        return '<id {}>'.format(self.id)    
    
    def serializer(self):
        return{
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'published': self.published
        }