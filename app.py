import os
from urllib import request
from flask import Flask, request, jsonify
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

# add Book function 
@app.route('/add', methods=['POST'])
def add_book():
    book_data = request.json
    
    name = book_data['name']
    author = book_data['author']
    published = book_data['published']
    print(name, author, published)
    
    try:
        book = Book(
            name=name,
            author=author,
            published=published
        )
        db.session.add(book)
        db.session.commit()
        return "Book added. book id={}".format(book.id)
    except Exception as e:
        return (str(e))
    
   
@app.route('/getall')
def get_all():
    try:
        books = Book.query.all()
        return  jsonify([e.serializer() for e in books])
    except Exception as e:
        return (str(e))   
    
@app.route("/name/<name>")
def get_book_name(name):
    return "name : {}".format(name)

@app.route("/details")
def get_book_details():
    author = request.args.get('author')
    published = request.args.get('published')
    return "Author : {}, Published: {}".format(author, published)

@app.route('/book/<id_>')
def get_bookid(id_):
    book_id = Book.query.filter_by(id=id_).first()
    return jsonify(book_id.serializer())

db.create_all()
if __name__ == '__main__':
    app.run()