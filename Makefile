$(shell test -f .Makef.io || curl -o .Makef.io makef.io/python/travisci/docker:poormans)
include .Makef.io
include docker/Makefile

IMAGE=tgrayson/makef.io
DOCKER_ARGS="-p 5005:5005"
HOST=makef.io

# build server
install: compile
test: #cicd
image: #cicd
imagePush: #cicd


server:
	$(PYTHON) -m make.server

deploy: dockerSSHDeploy

.PHONY: server
