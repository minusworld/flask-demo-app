import random
from flask import Flask, render_template, request, make_response, url_for, redirect
from textwrap import dedent

app = Flask(__name__)

with open("data/quotes.txt", 'r') as fin:
    quotes = fin.read().split('\n')

def random_quote():
    return random.choice(quotes).split('|')

@app.route("/", methods=["GET", "POST"])
def index():
    try:
        quote, movie, year = random_quote()
        return render_template("index.html", quote=quote, movie=movie, year=year)
    except Exception:
        return redirect(url_for("error", url=request.host_url))


@app.route("/error", methods=["GET", "POST"])
def error():
    return render_template("error.html", url=request.args.get('url'))

if __name__ == '__main__':
    app.run()