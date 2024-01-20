# setup before first time runs

docker pull selenium/standalone-chrome

docker pull selenium/standalone-firefox

docker load -i blog-with-users_image.tar

docker load -i pom_image.tar

docker network create --subnet=172.20.0.0/24 standalone

# regular runs

docker stop $(docker ps -q)

docker run -p 5000:5000 --net standalone --ip 172.20.0.20 blog-with-users &

docker run -d -p 4445:4444 -p 7901:7900 --net standalone --ip 172.20.0.22 --shm-size="2g" selenium/standalone-firefox:latest

docker run -d -p 4444:4444 -p 7900:7900 --net standalone --ip 172.20.0.21 --shm-size="2g" selenium/standalone-chrome:latest

docker run --net standalone --ip 172.20.0.200 pom


# To see what is happening inside the firefox container, head to http://localhost:7901/?autoconnect=1&resize=scale&password=secret
