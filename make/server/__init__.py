from flask import Flask, redirect
from reader import read

from make.config import TARGET_HOST


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
