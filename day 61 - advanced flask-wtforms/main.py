from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import email_validator
from flask_bootstrap import Bootstrap4
#----
import os
SECRET_KEY = os.urandom(32) #utf-8?
PASSWORDS = []
USERNAMES = []


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
bootstrap = Bootstrap4(app)
app.config['SECRET_KEY'] = SECRET_KEY




class MyForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField(label="Log In", validators=[DataRequired()])


@app.route("/")
def home():
    return render_template('index.html')


#NOTE:
#I SKIPPED A CHALLENGE
# CHALLENGE: Using the documentation on WTForm validators,
#  add Email validation to the email field so that you must type a valid email (with "@" and ".") otherwise you get an error.
#  Also add Length validation to the password, so you must type at least 8 characters.
# e.g. Email without "@" and 4 character password:
@app.route("/login", methods=["GET", "POST"])
def login():
    """Challenge
    Create the login route which renders the login.html file.
    Run the app to make sure it works. This is what you should see when you run it:"""
    form = MyForm()
    # form.validate_on_submit()
    # print(form.email.data)
    # print(form.password.data)
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return redirect('/success')
        else:
            return redirect('/denied')
    return render_template("login.html", form=form)

@app.route("/success", methods=["GET", "POST"])
def success():
    return render_template("success.html")

@app.route("/denied", methods=["GET", "POST"])
def denied():
    return render_template("denied.html")

if __name__ == '__main__':
    app.run(debug=True)

# 		<form method="POST" action=""> <!--removed action it fucked with it {{ url_for('success') }}-->
# 			{{ form.csrf_token }}
# 			<p>
# 				{{ form.email.label }} <br> {{ form.email(size=30) }}
# 				{% for err in form.email.errors %}
# 				<span style="color:red">{{ err }}</span>
# 				{% endfor %}
# 			</p>
# 			<p>
# 				{{ form.password.label }} <br> {{form.password(size=30) }}
# 				{% for err in form.email.errors %}
# 				<span style="color:red">{{ err }}</span>
# 				{% endfor %}
# 			</p>
# 			{{ form.submit }}
# 		</form>