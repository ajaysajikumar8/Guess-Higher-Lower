from flask import Flask
import random

app = Flask(__name__)

num = random.randint(0,9)
print(num)

@app.route("/")
def home():
    return "<h1><strong>Enter a number between 0 and 9</strong></h1>"\
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/<int:number>")
def check_num(number):
    if number == num:
        return "<h1 style='color:green'>You found me!</h1>"\
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif number > num:
        return "<h1 style='color:violet'>Too high, try again!</h1>"\
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1 style='color:red'>Too low, Try again!</h1>"\
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
if __name__ == "__main__":
    app.run(debug=True)       