from flask import Flask, redirect
from reader import read

TARGET_HOST = "https://raw.githubusercontent.com/trevorgrayson/Makefiles/master/%s/Makefile"

app = Flask(__name__)


@app.route('/<path:path>')
def many(path):
    words = str(path).split('/')
    make = read(*words)

    return make


@app.route('/<path:path>')
def redir(path):
    return redirect(TARGET_HOST % path)

@app.route('/')
def welcome():
    return "welcome"
