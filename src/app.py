import flask
import time

app = flask.Flask(__name__)

# testing123


@app.route("/")
def index():
    return "Welcome!!! ", time.localtime
