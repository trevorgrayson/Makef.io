docker:
	docker build .

dockerPackage:
	docker save -o $(PROJECT).tar $(TAG)

dockerPublish: 
	scp $(PROJECT).tar $(HOST):~
	
dockerSSHDeploy:
	echo "not implemented"
	# curl makef.io/docker:poormans/ssh-deploy.sh | sh
