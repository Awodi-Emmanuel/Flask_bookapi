import os
from urllib import request
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.init_app(app)


from models.models import Book

@app.route("/")
def hello():
    return "Hello"


@app.route("/name/<name>")
def get_book_name(name):
    return "name : {}".format(name)

@app.route("/details")
def get_book_details():
    author = request.args.get('author')
    published = request.args.get('published')
    return "Author : {}, Published: {}".format(author, published)

db.create_all()
if __name__ == '__main__':
    app.run()