import random
from flask import Flask, render_template_string, request, make_response, url_for, redirect
from textwrap import dedent

app = Flask(__name__)

with open("data/quotes.txt", 'r') as fin:
    quotes = fin.read().split('\n')

def random_quote():
    return random.choice(quotes).split('|')

@app.route("/", methods=["GET", "POST"])
def index():
    template = """
    <html><body>
    <h1>Random Movie Quotes</h1>
    <div>
      <h2>{}</h2>
      <h4>~{}, {}</h4>
    </div>
    </body></html>
    """
    try:
        return render_template_string(template.format(*random_quote()))
    except Exception:
        return redirect(url_for("error", url=request.host_url))


@app.route("/error", methods=["GET", "POST"])
def error():
    template = """
    <html><body>
    <h1>Error: Page not found.
      <a href="{}">Go back</a>
    </h1>
    </body></html>
    """
    resp = make_response(render_template_string(template.format(request.args.get('url'))))
    #resp.headers['Content-Security-Policy'] = "script-src https:"
    return resp

if __name__ == '__main__':
    app.run()