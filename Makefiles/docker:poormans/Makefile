docker:
	docker build .

dockerPackage:
	docker save -o $(PROJECT).tar $(TAG)

dockerPublish: 
	scp $(PROJECT).tar $(HOST):~

dockerSSHDeploy:
	ssh -t $(HOST) -X "docker stop $(HOST); docker rm $(HOST); docker rmi $(IMAGE); docker run --name $(HOST) --restart always -d $(DOCKER_ARGS) $(IMAGE)"
