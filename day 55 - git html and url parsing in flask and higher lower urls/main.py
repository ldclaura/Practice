from flask import Flask

app = Flask(__name__) #__name__
print(__name__) #prints __main__

@app.route("/") #"/" is home route, the first location.
#the @ in @app.route is a python decorator

def bold_decorator(function):
    def wrapper_function():
        return "<b>" + function() + "</b>"
    return wrapper_function

def hello_world():
    """http://127.0.0.1:5000 (home)"""
    return "<p>Hello, World!</p>"
#NOTE it wont work if inside another folder.
@app.route("/bye")
@bold_decorator #doesnt work with arguments in func??
def goodbye_world():
    """http://127.0.0.1:5000/bye"""
    return "Goodbye, World :c" #you don't necessarily need the <p></p>

@app.route("/user/<greest>/123") #<the name of parameter of function>
#the <thing> can be between multiple other locations (/user/<whateveryouwant>/blahblah)
def greeting(greet): #the decorator takes the param
    """http://127.0.0.1:5000/user/(basically anything)/123"""
    return f"{greet}" #itll show whatever u put into the link after /user/

@app.route("/username/<path:name>") #if name is laura/hj it will allow it
def path(name):
    """http://127.0.0.1:5000/username/yourname/whateverthefuckelseyouwrite"""

@app.route("/birthday/<birthdayname>/<int:age>")
def happy_birthday(birthdayname, age):
    """http://127.0.0.1:5000/birthday/laura/21"""
    return f"happy birthday {birthdayname}, you are {age}!"



@app.route("/html/<thetitle>")

def some_fancy_html(thetitle):
    """http://127.0.0.1:5000/html/thetitleyouput"""
    return f"<h1 style='text-align: center'>{thetitle}</h1>" \
    "<p>and now a paragraph</p>" \
    "<p>you can split using a backslash to make it easier to read</p>" \
    "<img src=https://media.giphy.com/media/agFnhoKCNc9bSSsGtd/giphy.gif?cid=ecf05e47f1h5sv1x7246k3dv8lja9h95g3osggfkudyk5w29&ep=v1_gifs_search&rid=giphy.gif&ct=g>"



if __name__ == "__main__":
    app.run() #runs without the terminal and cmd SHIT
    #DEBUG MODE
    # app.run(debug=True)
    #in debug mode the website detects changes in code and updates automatically.
    #it will also give you a webpage that shows you an error message if you fuck something up
    #e.g TypeError
    # TypeError: greeting() got an unexpected keyword argument 'greest' (parameter name didn't match the app.route input)
    #so basically what you get when you fuck up in terminal or powershell

    #when you launch the website in debug mode you'll get a pin
    #you can use this pin when you click the lil terminal button on an error website they give you
    #you get to open terminal and fuck around with it to figre out whats wrong
    


