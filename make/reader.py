from os.path import exists
from functools import reduce

from make import Makefile


def path(word):
    return "Makefiles/%s/Makefile" % word


def read(*args):
    mks = []

    for arg in args:
        p = path(arg)

        if exists(p):
            with open(p, 'r') as fp:
                mks.append(Makefile.parse(fp.readlines()))
        else:
            p = path(args[0] + '/' + arg)

            if exists(p):
                with open(p, 'r') as fp:
                    mks.append(Makefile.parse(fp.readlines()))
        
    return reduce(lambda a,b: a+b, mks).render()

def replace_opts(make, **opts):
    lines = make.split("\n")
    ii = 0

    while ii < len(lines):
        sp = lines[ii].split("?=")
        if len(sp) > 0 and sp[0] in opts.keys():
            lines[ii] = f"{sp[0]}?={opts.get(sp[0])}"

        ii += 1

    return "\n".join(lines)
