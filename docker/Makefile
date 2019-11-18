# IMAGE
# DOCKER_USER DOCKER_PASS

image: 
	@[ "${IMAGE}" ] || (echo "define docker IMAGE name"; exit 1)
	docker build -t $(IMAGE) .

imagePush:
	@[ "${IMAGE}" ] || (echo "define docker IMAGE name"; exit 1)
	echo "$(DOCKER_PASS)" | docker login -u "$(DOCKER_USER)" --password-stdin
	docker push $(IMAGE)
