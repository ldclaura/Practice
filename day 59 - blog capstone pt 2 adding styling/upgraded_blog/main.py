from flask import Flask, render_template
import requests

app = Flask(__name__)
API = "https://api.npoint.io/3935a5ca23df5901f399"
RESPONSE = requests.get(API)
ALL_POSTS = RESPONSE.json()

@app.route("/")
def home():
    return render_template("index.html", posts=ALL_POSTS)
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post/<int:num>")
def post(num):
    return render_template("post.html", posts=ALL_POSTS, ID=num)
#in the html i was trying to do {{ url_for('post', ID=post['id']) }} instead of {{ url_for('post', num=post['id']) }}
if __name__ == "__main__":
    app.run(debug=True)
