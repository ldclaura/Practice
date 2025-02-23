#NOTE make sure your py file isn't the same as an import (library/framework, no requests.py, no flask.py)
#client
#server
#database

#library = BeautifulSoup
#framework = django
#library = you are in full control when you call a method from a library and the control is then returned
#framework = the code never calls into a framework, instead the framework calls you


from flask import Flask

app = Flask(__name__) #__name__
print(__name__) #prints __main__

@app.route("/") #"/" is home route, the first location.
#the @ in @app.route is a python decorator
def hello_world():
    """http://127.0.0.1:5000 (home)"""
    return "<p>Hello, World!</p>"
#NOTE it wont work if inside another folder.
@app.route("/bye")
def goodbye_world():
    """http://127.0.0.1:5000/bye"""
    return "Goodbye, World :c" #you don't necessarily need the <p></p>


if __name__ == "__main__":
    app.run() #runs without the terminal and cmd SHIT

#running in terminal or Python
#$env:FLASK_APP="hello.py"
#flask run

#running in cmd (command prompt)
#set FLASK_APP=hello.py
#flask run

#command prompt
#cd (shows where u r)
#cd Desktop (puts u in desktop)
#mkdir HelloWorld (creates folder in location called HelloWorld)
#cd HelloWorld (puts you into the folder you just created, from Desktop (if ur still in desktop))
#dir (shows list of whats in the location you're in)
#echo. > main.py (creates main.py file in current directory/folder)
#del main.py (deletes file)
#cd .. (sends you two steps up, back into desktop)
#cd C:\Users\laura\Desktop (this also works)
#rmdir Test (deletes folder)
#rd Test (also works)