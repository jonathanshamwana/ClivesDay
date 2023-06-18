from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
import requests

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/photo")
def gallery_photo():
    return render_template("gallery-single.html")

@app.route("/fetch-joke", methods=["GET", "POST"])
def joke():

    joke_url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "text/plain"}
    response = requests.get(url=joke_url, headers=headers)
    dad_joke = response.text

    return render_template("joke.html", dad_joke=dad_joke)

if __name__ == "__main__":
    app.run(debug=True,port=5000)
