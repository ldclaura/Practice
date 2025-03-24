from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, select
from sqlalchemy.sql import text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass

# CREATE TABLE
db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
db.init_app(app)

class Movies(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    year: Mapped[int] = mapped_column(unique=False, nullable=False)
    description: Mapped[str] = mapped_column(unique=False, nullable=False)
    rating: Mapped[float] = mapped_column(unique=False, nullable=True)
    ranking: Mapped[int] = mapped_column(unique=True, nullable=True)
    review: Mapped[str] = mapped_column(unique=False, nullable=True)
    img_url: Mapped[str] = mapped_column(unique=False, nullable=False)


with app.app_context():
    db.create_all()

# with app.app_context():
#     new_movie = Movies(
#         title="Phone Booth",
#         year=2002,
#         description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#         rating=7.3,
#         ranking=10,
#         review="My favourite character was the caller.",
#         img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
#     )
#     db.session.add(new_movie)
#     db.session.commit()

class UpdateMovieForm(FlaskForm):
    rating = StringField('Rating', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])
    submit = SubmitField('Submit')

def bubble_sort_backwards(arr):
    """This is bubble sort algorithm but backwards"""
    for n in range(len(arr), 0, -1):# for n in range(len(arr) -1, 0, -1):

        swapped = False

        for i in range(len(arr)-1, len(arr)-n, -1):#for i in range(n):
            if arr[i-1] < arr[i]: #if arr[i] < arr[i + 1]:

                arr[i], arr[i - 1] = arr[i - 1], arr[i]#arr[i], arr[i + 1] = arr[i + 1], arr[i]

                swapped = True
        if not swapped:
            break
def bubble_sort(arr):
    """This is bubble sort algorithm but backwards"""
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):
        
        # Initialize swapped to track if any swaps occur
        swapped = False  

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:
              
                # Swap elements if they are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                
                # Mark that a swap has occurred
                swapped = True
        
        # If no swaps occurred, the list is already sorted
        if not swapped:
            break


@app.route("/")
def home():
    movies = db.session.query(Movies).all()

    ratingordered = []
    for _ in movies:
        ratingordered.append(_.rating)
    bubble_sort(ratingordered) #the ratings in order worst to best
    rank = 10
    for x in ratingordered:
        try:
            movies2 = db.session.execute(select(Movies).filter_by(rating=x)).scalar_one()
            movies2.ranking = rank
            db.session.commit()
        except:
            pass
        rank - 1
    movies = db.session.query(Movies).all()
    return render_template("index.html", movies=movies)

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    # movies = db.session.query(Movies).all()
    movies = db.session.execute(select(Movies).filter_by(ranking=id)).scalar_one()
    form = UpdateMovieForm()
    if form.validate_on_submit():
        movies.rating = form.rating.data
        movies.review = form.review.data
        db.session.commit()
        return redirect("/")
    return render_template("edit.html", id=id, form=form)

if __name__ == '__main__':
    app.run(debug=True)
