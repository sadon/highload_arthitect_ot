# Highload Architect Otus

## Homework 1
1. Create Api
2. Create Postman collection

Methods:
/login
/user/register
/user/get/{id}

Desc:
Фронт опционален.
Сделать инструкцию по локальному запуску приложения, приложить Postman-коллекцию.
ДЗ принимается в виде исходного кода на github и Postman-коллекции.


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

# Docker compose start
cd highload_arthitect_ot
docker compose up --build

http://localhost:8000 - Main application
psql: localhost:8432 Postgresc DB: database


---

# Start local server 
`uvicorn sql_app.main:app --reload`


# Post example
{
  "email": "test-2@example.com",
  "password": "test",
  "first_name": "Dmitry",
  "second_name": "Dubovitskiy",
  "birthday": "1985-05-1985",
  "male_sign": true,
  "biography": "races, languages, python",
  "city": "Belgrade"
}
