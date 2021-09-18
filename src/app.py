import flask
import time

app = flask.Flask(__name__)

# testing


@app.route("/")
def index():
    return "Welcome!!! ", time.localtime
