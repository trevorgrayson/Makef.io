from flask import Flask, redirect
from reader import read

TARGET_HOST = "https://raw.githubusercontent.com/trevorgrayson/Makefiles/master/%s/Makefile"


app = Flask(__name__)

@app.route('/<path:path>')
def redir(path):
    words = str(path).split('/')
    make = read(*words)

    return make

    # return redirect(TARGET_HOST % path)

@app.route('/')
def welcome():
    return "welcome"


if __name__ == '__main__':
    app.run('0.0.0.0', port=5005)
