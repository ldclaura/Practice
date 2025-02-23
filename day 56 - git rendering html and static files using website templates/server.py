from flask import Flask, render_template
#render_template is for rendering html files
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html") #<-- grabs html file from templates folder
    # has to be from templates folder, has to be called templates.



if __name__ == "__main__":
    app.run(debug=True)

#NOTE: some servers don't allow 4 letter file extentions so html becomes htm
#it still works as htm but i'd change it

#NOTE: chrome likes to save cache static files,
#when you visit a website if you visit same day its unlikely to change, 
#so chrome saves the website you download so it doesnt have to download again
#shift + reload page = hard reload. redownloads page and gets rid of cache files.

#NOTE
#inspect, console
#document.body.contentEditable=true (javascript)
#(lower t for true)
#can now edit anything on website, delete stuff, (doesnt save tho)