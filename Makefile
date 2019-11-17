# $(shell curl -o python.Makefile https://raw.githubusercontent.com/trevorgrayson/Makefiles/master/python/Makefile)
include python.Makefile

server:
	$(PYTHON) -m server

.PHONY: server
# $(shell curl -o python.Makefile make.org/python/flask?PYTHON=python3)
