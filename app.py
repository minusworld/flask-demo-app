from flask import Flask, render_template_string, request, make_response
from textwrap import dedent

app = Flask(__name__)

@app.route("/error", methods=["GET", "POST"])
def error():
    template = """
    <html><body>
    <h1>Error: Page not found.
      <a href="{}">Go back</a>
    </h1>
    </body></html>
    """
    resp = make_response(render_template_string(dedent(template).format(request.args.get('url'))))
    return resp

app.run()
