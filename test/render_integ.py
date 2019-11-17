from functools import reduce
from flask import Flask, redirect

from make.proxy_client import ProxyClient
from make import Makefile
from make.config import TARGET_HOST

CLIENT = ProxyClient(TARGET_HOST)


class TestInteg:

    def test_fetch_and_render(self):
        words = ['python']

        docs = [(CLIENT.read(word).split("\n")) for word in words]

        mks = [Makefile.parse(mk) for mk in docs if mk]
        make = reduce(lambda a, b: a + b, mks)
        print(mks[0].render())
