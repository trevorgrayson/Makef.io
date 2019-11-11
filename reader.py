from os.path import exists


def path(word):
    return "%s/Makefile" % word


def read(*args):
    out = ""
    pathes = []

    for arg in args:
        p = path(arg)

        if exists(p):
            with open(p, 'r') as fp:
                out += fp.read()
        else:
            p = path(args[0] + '/' + arg)

            if exists(p):
                with open(p, 'r') as fp:
                    out += fp.read()
        
    return out

def replace_opts(make, **opts):
    lines = make.split("\n")
    ii = 0

    while ii < len(lines):
        sp = lines[ii].split("?=")
        if len(sp) > 0 and sp[0] in opts.keys():
            lines[ii] = f"{sp[0]}?={opts.get(sp[0])}"

        ii += 1

    return "\n".join(lines)
