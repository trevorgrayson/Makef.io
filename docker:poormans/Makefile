docker:
	docker build .

dockerPackage:
	docker save -o $(PROJECT).tar $(TAG)

dockerPublish: 
	scp $(PROJECT).tar $(HOST):~
	
