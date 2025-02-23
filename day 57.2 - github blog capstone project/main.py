from flask import Flask, render_template
import requests

#https://www.npoint.io/
FAKE_BLOGS = "https://api.npoint.io/c790b4d5cab58020d391"
RESPONSE = requests.get(FAKE_BLOGS)
ALL_POSTS = RESPONSE.json()
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=ALL_POSTS)

@app.route('/blog/<int:num>')
def blog(num):
    return render_template("post.html", posts=ALL_POSTS, ID=num)

# <!--            {{% for post in posts %}}
#                     {{% if post["id"] == 1 %}}
#                         <h2>{{% post["title"] %}}</h2>
#                         <p>{{% post["body"] %}}</p>
#                     {{% else %}}
#                         {{% endif %}}
#                 {{% endfor %}}-->  
#NOTE THIS CODE ABOVE IS WRONG
#NOTE {{ post["title"] }} NOT {{% post["title"] %}}
#I added unneccessary %, that's why it didnt work.




if __name__ == "__main__":
    app.run(debug=True)
