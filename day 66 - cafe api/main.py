from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, select
import random
import requests
'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        """Convert Cafe object into a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "map_url": self.map_url,
            "img_url": self.img_url,
            "location": self.location,
            "seats": self.seats,
            "has_toilet": self.has_toilet,
            "has_wifi": self.has_wifi,
            "has_sockets": self.has_sockets,
            "can_take_calls": self.can_take_calls,
            "coffee_price": self.coffee_price,
        }


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    print(db.session.execute(db.select(Cafe)).scalars())
    print(db.get_or_404(Cafe, 2).name)
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random", methods=["GET"]) #if method is not specified, then it is automatically GET
def randomcafe(): #i made it def random before and then realised my mistake
    """randomly picks cafe and returns that json"""
    total_items = db.session.query(Cafe).count()
    random_id = random.randint(0, total_items)
    random_cafe = db.session.execute(db.select(Cafe).filter(Cafe.id == random_id)).scalars().all()
    try:
        return jsonify(cafe=[cafe.to_dict() for cafe in random_cafe])
    except UnboundLocalError:
        return jsonify(error={"Not Found":"Sorry, we don't have a cafe at that location"})

@app.route("/all")#if method is not specified, then it is automatically GET
def allcafe():
    """ALL CAFES"""
    all_cafes = db.session.query(Cafe).all()
    return jsonify(cafe=[cafe.to_dict() for cafe in all_cafes])

@app.route("/search", methods=["GET"])#if method is not specified, then it is automatically GET
def search_cafe():
    """Custom Location Search"""
    location = request.args.get("loc")#localhost:5000/search?loc=Peckham
    print(location)
    locationsortedcafes = db.session.execute(db.select(Cafe).filter(Cafe.location == location)).scalars().all()
    try:
        return jsonify(cafe=[cafe.to_dict() for cafe in locationsortedcafes])
    except UnboundLocalError:
        return jsonify(error={"Not Found":"Sorry, we don't have a cafe at that location"})


# HTTP POST - Create Record
@app.route("/add", methods=["POST", "GET"]) #methods=["POST"] and GET, need GET to return response.
def add_cafe():
    if request.method == "POST":
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("loc"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success":"Successfully added the new cafe."})

# HTTP PUT/PATCH - Update Record
#u have broken bike
#put is sending new bike, entirely new entry
#patch is only sending new wheel, only sending piece that needs to be updated, not whole thing
@app.route("/update-price/<cafe_id>", methods=["PATCH", "GET"])
def update_coffee_price(cafe_id):
    if request.method == "PATCH":
        #put as query params in postman, not body
        #http://127.0.0.1:5000/update-price/3?new_price=£7.00
        updatedprice = request.args.get("new_price") #£
        idsortedcafes = db.session.execute(db.select(Cafe).filter(Cafe.id == cafe_id)).scalar_one()
        idsortedcafes.coffee_price = updatedprice
        db.session.commit()
        return jsonify(response={"success":"Successfully updated the coffee price."})
# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>", methods=["DELETE", "GET"])
def delete_cafe(cafe_id):
    APIKey = "TopSecretAPIKey"
    if request.method == "DELETE":
        if request.args.get("api-key") == APIKey:
            try:
                idsortedcafes = db.session.execute(db.select(Cafe).filter(Cafe.id == cafe_id)).scalar_one()
            except:
                return jsonify({"error":{"Not Found":"Sorry a cafe with that id was not found in the database."}}), 404
            db.session.delete(idsortedcafes)
            db.session.commit()
            return jsonify(response={"success":"Successfully deleted the cafe."})
        else:
            return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api_key"), 403 #wrong api key
        # return jsonify({"error":{"Not Found":"Sorry a cafe with that id was not found in the database."}}) #non existing id


if __name__ == '__main__':
    app.run(debug=True)


#NOTE
# REpresentational State Transfer - REST


# client -> server
# http request to server (language used to make request)
# or maybe ftp request (file transfer protocol)

# http = French - ftp = Italian, basically make sure you use same protocol.

# API is like a menu

# REST = architectural style
# baroque, gothic, neoclassical
# architectural style for designing APIs

# SOAP, GraphQL, Falcor - example of others

# REST is gold standard


# RESTFUL RULES:

# USE HTTP REQUEST VERBS
# get, post, put, patch(new), delete
# USE SPECIFIC PATTERN OF ROUTES/ENDPOINT URLs
# GET /articles - fetches ALL articles /articles/jack-bauer - fetches THE article on jack-bauer
# POST /articles - creates one new article
# PUT /articles/jack-bauer - updates the article on jack-bauer
# PATCH /articles/jack-bauer - updates the article on jack-bauer
# DELETE /articles - delete all the articles /articles/jack-bauer - deletes the article on jack bauer

# {
#     "cafe": {
#         "can_take_calls": true,
#         "coffee_price": "£2.60",
#         "has_sockets": true,
#         "has_toilet": false,
#         "has_wifi": true,
#         "id": 17,
#         "img_url": "https://lh3.googleusercontent.com/p/AF1QipOZ3WDAAxphLu657afVVATJ5TGxtturIOr8gt8u=s0",
#         "location": "Whitechapel",
#         "map_url": "https://goo.gl/maps/xv29seioiETAAZgN9",
#         "name": "Whitechapel Grind",
#         "seats": "30-40"
#     }
# }