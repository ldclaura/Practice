from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
import smtplib
MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")
PRIVATE_EMAIL = os.getenv("PRIVATE_EMAIL")

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


def email_response(request):
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=PRIVATE_EMAIL, msg=f"""Subject:Contact Submission\nName: {request['name']}\nEmail: {request['email']}\nPhone: {request['phone']}\nMessage: {request['message']}""")
    except:
        print("Failed to send")
    finally:
        print("COMPLETED")

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact", methods=["POST"])
def receive_data():
    if request.method == "POST":
        result = request.form.to_dict()
        print(f"""{result['name']}\n{result['email']}\n{result['phone']}\n{result['message']}""")
        #---
        email_response(result)
        #---
        return render_template("form-entry.html", result=result)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
