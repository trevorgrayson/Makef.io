docker stop $(CONTAINER)
docker rm $(CONTAINER)
docker rmi $(IMAGE)
docker run $(DOCKER_ARGS) $(IMAGE)
