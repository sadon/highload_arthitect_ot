# Highload Architect Otus

# Инструкция по запуску docker-compose
```
git clone https://github.com/sadon/highload_arthitect_ot
cd highload_arthitect_ot
docker compose up --build`
```

Далее браузер [http://localhost:8000/docs](http://localhost:8000/docs)
![openapi.png](openapi.png)





---

## Домашнее задание 1. Постановка:
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













---
# Справка для локального запуска

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

## Docker compose start
```
cd highload_arthitect_ot
docker compose up --build
```

- http://localhost:8000 - Main application
- psql: localhost:8432 Postgres DB: database

## Start server locally: 
`cd python-engine`
`uvicorn sql_app.main:app --reload`


## Post example
```commandline

{
  "email": "test@example.com",
  "password": "test",
  "first_name": "Dmitry",
  "second_name": "Dmitriev",
  "birthday": "2000-05-09",
  "male_sign": true,
  "biography": "races, languages, python",
  "city": "Belgrade"
}
```