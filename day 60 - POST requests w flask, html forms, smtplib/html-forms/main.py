from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/") #methods=['GET', 'POST']
def home():
    return render_template("index.html")

@app.route("/login", methods=['POST']) #methods=['GET', 'POST']
def receive_data():
    if request.method == "POST":
        result = request.form.to_dict()
        return render_template("login.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)