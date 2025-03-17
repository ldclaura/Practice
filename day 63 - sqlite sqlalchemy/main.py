from flask import Flask, render_template, request, redirect, url_for
#NOTE TO SELF, DON'T USE PYTHON3.13.2
#STICK WITH 3.11.9!!!
#PLEASE LISTEN TO ME!!
#I WAS AN IDIOT I COULDNT INSTALL THINGS SO I THOUGHT THAT DELETING MY TMP VARIABLE WOULD FIX IT
#IM A BIT RETARDED I THOUGHT IT WAS THE SAME AS TEMP BUT SPELT WRONG LOL
#I MADE A NEW ONE BUT THAT WAS AFTER INSTALLING PYTHON3.13.2 BECAUSE I THOUGHT IT BEING OUTDATED WAS THE PROBLEM
#THEN I SPENT AGES TRYING TO FIGURE OUT WHY THE GREENLET WOULDNT INSTALL FLASK SQLALCHEMY
#THEN I JUST WENT BACK TO PYTHON3.11.9 AND IT WORKS NOW
#FUCK ME
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, insert

#NOTE CRUD data
#create, read, update, delete
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

all_books = []


app = Flask(__name__)

#db are stored in instance folder, this makes instance folder.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
db.init_app(app)


class Book_Collections(db.Model): #the class name is the name of the table when viewing in sqlite db browser
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=False)
    author: Mapped[str] = mapped_column(unique=False)
    rating: Mapped[int] = mapped_column(unique=False)
# sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError) UNIQUE constraint failed: book__collections.rating
# [SQL: INSERT INTO book__collections (title, author, rating) VALUES (?, ?, ?)]
# [parameters: ('Metamorphosis', 'Franz Kafka', '9')]
# (Background on this error at: https://sqlalche.me/e/20/gkpj)
#this error happens when i try to give a book same author or same rating as another book. 

with app.app_context():
    db.create_all()

def delete(id):
    Book_Collections.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect("/")

@app.route('/', methods=["POST", "GET"])
def home():
    # for _ in all_books:
    #     print(_) #{'title': 'IT', 'author': 'Stephen King', 'rating': '10'}
    #     for x in _:
    #         print(x) #title author rating
    db_books = db.session.query(Book_Collections).all()
    print(db_books)

    for entry in db_books:
        print(entry.__dict__)
    remove = delete(1)
        #{'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x000001C0E2CD3530>, 'rating': 8, 'id': 1, 'title': 'IT', 'author': 'Stephen King'}
    # author = db.session.get(Book_Collections, "author")
    # rating = db.session.get(Book_Collections, "rating")
    return render_template("index.html", all_books=all_books, db_books=db_books, remove=remove) #NOTE i spent ages and finally realised that the reason it didn't work
    #is because i didnt do all_books=all_books (aka returned it)
#{{ x['rating'] }}

@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        result = request.form.to_dict()
        title = result.get('title')
        author = result.get('author')
        rating = result.get('rating')
        new_book = Book_Collections(title=title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()

        all_books.append(result)
        print(all_books)
        return redirect("/")
    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["POST", "GET"])
def change_rating(id):
    bookrating = Book_Collections.query.filter_by(id=id).first()
    print(bookrating.__dict__)
    editentry = bookrating.__dict__
    if request.method == "POST":
        result = request.form.to_dict()
        rating = result.get('rating')
        bookrating.rating = rating
        db.session.commit()
        return redirect("/")

    return render_template("edit.html", editentry=editentry)



if __name__ == "__main__":
    app.run(debug=True)

