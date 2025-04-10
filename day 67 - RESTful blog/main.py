from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''




app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
app.config['CKEDITOR_HEIGHT'] = 1000
app.config['CKEDITOR_WIDTH'] = 1000
ckeditor = CKEditor(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    requested_post = db.session.execute(db.select(BlogPost).filter(BlogPost.id == post_id)).scalar()
    return render_template("post.html", post=requested_post)


# TODO: add_new_post() to create a new blog post
@app.route('/new-post', methods=["POST", "GET"])
def add_new_post():
    if request.method == 'POST':
        new_post = BlogPost(
            title=request.form.get("title"),
            subtitle=request.form.get("subtitle"),
            date=str(date.today().strftime('%B %d, %Y')),
            body=request.form.get("ckeditor"),
            author=(request.form.get("author")),
            img_url=(request.form.get("img_url")),
        )
        db.session.add(new_post)
        db.session.commit()
    return render_template("make-post.html")
# TODO: edit_post() to change an existing blog post
@app.route('/edit-post/<post_id>', methods=["POST", "GET"])
def edit_post(post_id):
    requested_post = db.session.execute(db.select(BlogPost).filter(BlogPost.id == post_id)).scalar_one()
    if request.method == "POST":
        requested_post.title=request.form.get("title")
        requested_post.subtitle=request.form.get("subtitle")
        requested_post.date=str(date.today().strftime('%B %d, %Y'))
        requested_post.body=request.form.get("ckeditor")
        requested_post.author=(request.form.get("author"))
        requested_post.img_url=(request.form.get("img_url"))
        db.session.commit()
    return render_template("make-post.html")
# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<post_id>', methods=["DELETE", "GET"])
def delete_post(post_id):
    try:
        requested_post = db.session.execute(db.select(BlogPost).filter(BlogPost.id == post_id)).scalar_one()
    except:
        print("nah")
    db.session.delete(requested_post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
