docker stop $PROJECT; 
docker rm $PROJECT; 
docker rmi $IMAGE; 
docker run --name $PROJECT $DOCKER_ARGS -d --restart=always $IMAGE"
