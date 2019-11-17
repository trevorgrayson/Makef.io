$(shell test -f python.Makefile || curl -o python.Makefile mk.tacks.me/python/travisci)
include python.Makefile

server:
	$(PYTHON) -m make.server

.PHONY: server
