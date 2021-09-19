import flask
import time

app = flask.Flask(__name__)

# testing12334


@app.route("/")
def index():
    return "Welcome!!! ", time.localtime
