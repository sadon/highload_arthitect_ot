# Highload Architect Otus

## Homeworks
1. Create Api
2. Create Postman collection


## Postgres image
```commandline
$ cd database/
# Create the docker image 
$ docker build . 
# Run the docker image and connect to it
$ docker run -it <image_id> bash
# Enter to the database
psql postgres://username:secret@localhost:5432/database
```