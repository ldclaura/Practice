from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

with app.app_context():
    db.create_all()

# with app.app_context():
#     new_user = User(
#         email="laura@gmail.com",
#         password="password12345",
#         name="laura",
#     )
#     db.session.add(new_user)
#     db.session.commit()

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        new_user = User(
            email=request.form.get("email"),
            password=generate_password_hash(request.form.get("password"), method='pbkdf2', salt_length=8), #sha256
            name=request.form.get("name"),
        )
        name = request.form.get("name")
        if new_user.email != None:
            print("success")
            db.session.add(new_user)
            db.session.commit()
            login_user(load_user(new_user.id))
            return redirect(f'/secrets/{name}')
        else:
            print("dicks")
    return render_template("register.html")


@app.route('/login', methods=["POST", "GET"])
def login():
    password = False
    if request.method == "POST":
        email=request.form.get("email")
        try:
            requested_user = db.session.execute(db.select(User).filter(User.email == email)).scalar_one()
            password=check_password_hash(requested_user.password, request.form.get("password")) #sha256\
            if password == True:
                flash("success")
                login_user(load_user(requested_user.id))
            else:
                flash("Your password was incorrect, try again.")
        except:
            flash("Your email was incorrect, try again.")
    return render_template("login.html")


@app.route('/secrets/<name>', methods=["GET", "POST"])
@login_required
def secrets(name):
    return render_template("secrets.html", name=name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/download')
@login_required
def download():
    return send_from_directory("static/files", "cheat_sheet.pdf", as_attachment=True) #in html <a href="img.img" target="_blank">
    # target="_blank" is a special keyword that will open links in a new tab every time.
    # target="blank" will open the first-clicked link in a new tab, but any future links that share target="blank" will open in that same newly-opened tab.
    #however, i removed it because it opened then immediately closed the tab for some reason, so i thought it was unneccessary anyway


if __name__ == "__main__":
    app.run(debug=True)

#level 1 encryption - plain text password
#level 2 encryption - scrambling message and requiring key
#e.g. password qwerty, key 1 (1 shift), cipher method is caesar cipher, ciphertext is rvfsuz
#level 3 encryption - hashing
#level 4 encryption - hashing and salting
#password > salt password > hash the salted password
#bcrypt instead of MD5 hashing
#you can calculate 20,000,000,000 MD5 per second but only 17k bcrypt hashes per sec
#salt rounds - how many times salted, salt password, then salt hashed password, then run through encrypting, rinse and repeat.
#table contains | username | salt | hash x 10 |
#checking password - take password, conbine with salt, run it through same num of salting rounds until you get the final hashed password
#hashing removes the key
#encryptii.com
