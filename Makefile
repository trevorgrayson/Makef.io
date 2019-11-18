$(shell test -f .Makef.io || curl -o .Makef.io makef.io/python/travisci)
include .Makef.io

install: compile
test: #cicd

server:
	$(PYTHON) -m make.server

.PHONY: server
