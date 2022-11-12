#!/usr/bin/python3
"""
Routes:
  /: display “Hello HBNB!”
  /hbnb: display “HBNB”
  /c/<text>: display “C ” followed by
  the value of the text variable
  /python/(<text>): display “Python ”,
  followed by the value text variable
"""
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display HBNB!"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display C followed by the value text!"""
    text = text.replace("_", " ")
    return 'C %s' % text


@app.route("/python", strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text="is cool"):
    """display python followed by the value text!"""
    text = text.replace("_", " ")
    return 'Python %s' % text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
