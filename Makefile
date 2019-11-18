$(shell test -f .Makef.io || curl -o .Makef.io makef.io/python/docker/travisci)
include .Makef.io

IMAGE=tgrayson/makef.io

# build server
install: compile
test: #cicd


server:
	$(PYTHON) -m make.server

.PHONY: server
