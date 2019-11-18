$(shell test -f .Makef.io || curl -o .Makef.io makef.io/python/travisci)
include .Makef.io
include docker/Makefile

IMAGE=tgrayson/makef.io

# build server
install: compile
test: #cicd
image: #cicd
imagePush: #cicd


server:
	$(PYTHON) -m make.server

.PHONY: server
