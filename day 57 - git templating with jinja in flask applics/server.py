from flask import Flask, render_template
import random
import datetime
import requests

#jinja comes with flask no need to install jinja
app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1,19)
    datem = datetime.datetime.today().strftime("%Y")
    return render_template("index.html", num=random_number, year=datem) #MAKE SURE IN index.html TEMPLATES FOLDER
#return render_template can return as many variables you want, just need to set the name (num=random_number, name is num-var is random_number)
@app.route("/guess/<name>")
def guess(name):
    response = requests.get(url=f"https://api.genderize.io?name={name}")
    response2 = requests.get(url=f"https://api.agify.io?name={name}")
    r = response.json()
    r2 = response2.json()
    name = r["name"].title()
    gender = r["gender"]
    age = r2["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)

@app.route("/blog/<int:num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    print(all_posts)
    return render_template("blog.html", posts=all_posts)


    # <!--{{ single line expressions in python}}-->
#NOTE jinja parses comment lines, which means html comments will be read by jinja and will mess up your code
#do not use comments with jinja






if __name__ == "__main__":
    app.run(debug=True)