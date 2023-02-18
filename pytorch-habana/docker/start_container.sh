docker build -t pytorch-habana:latest -f docker/Dockerfile .
docker rmi $(docker images -f dangling=true -q)
docker run -it --rm --network=host -v $PWD/:/pytorch-habana --workdir /pytorch-habana pytorch-habana:latest
