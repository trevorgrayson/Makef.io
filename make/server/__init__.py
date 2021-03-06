from functools import reduce
from flask import Flask, redirect, Response

from make.proxy_client import ProxyClient
import make.reader
from make import Makefile
from make.config import TARGET_HOST

CLIENT = make.reader

app = Flask(__name__)

def headers():
    return {
        'Content-Type': 'text/Makefile'
    }

LANDING = open('public/index.html', 'r').read()

@app.route('/<path:path>')
def many(path):
    words = str(path).split('/')
    docs = [(CLIENT.read(word).split("\n\n")) for word in words]

    mks = [Makefile.parse(mk) for mk in docs]
    make = reduce(lambda a, b: a + b, mks)


    return Response(make.render(), headers=headers())


@app.route('/<path:path>')
def redir(path):
    return redirect(TARGET_HOST % path)


@app.route('/')
def welcome():
    return LANDING
