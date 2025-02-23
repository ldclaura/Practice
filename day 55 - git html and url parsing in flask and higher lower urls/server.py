from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0, 9)

def heading_decorator(function):
    #i tried to make this but it didnt work with both home and random number page.
    #something about them overriding eachother?
    #i checked solutions and yu didn't even make her own wrapper so i wont try
    #maybe she'll go more into it next lesson
    def wrapper():
        return "<h1>" + function() + "</h1>"
    return wrapper


print(random_number)
@app.route("/")

def home():
    return "<h1>Guess a number between 1 and 9</h1>" \
    "<img src='https://media.giphy.com/media/8lgqAbycBjosxjfi9k/giphy.gif?cid=790b7611q37sy0d2yuu9gwmijk6xqr8r3u68oulzfvpvkfto&ep=v1_gifs_trending&rid=giphy.gif&ct=g'>"


@app.route("/<int:randomnumber>")
def random_number_page(randomnumber):
    if randomnumber == random_number:
        return "<h1>You found me!</h1>" \
        "<img src='https://media.giphy.com/media/AAmhvrZzLCz1m/giphy.gif?cid=790b76110nmxzs79jk4hmb91w04kbpq1wlvsasirpe3hduiu&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
    elif randomnumber > random_number:
        return "<h1>Too high, try again</h1>" \
        "<img src='https://media.giphy.com/media/J6vo322gNemU4ilfDC/giphy.gif?cid=790b76110nmxzs79jk4hmb91w04kbpq1wlvsasirpe3hduiu&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
    elif randomnumber < random_number:
        return "<h1>too low, try again</h1>" \
        "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMG5teHpzNzlqazRobWI5MXcwNGticHExd2x2c2FzaXJwZTNoZHVpdSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/qs4ll1FSxKnNHeSmom/giphy.gif'>"


if __name__ == "__main__":
    app.run()