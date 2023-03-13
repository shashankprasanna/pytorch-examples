docker build -t pytorch2:latest -f docker/Dockerfile.gpu .
docker rmi $(docker images -f dangling=true -q)
docker run -it --rm --network=host --gpus all -v $PWD:/pytorch-examples --workdir /pytorch-examples pytorch2:latest
