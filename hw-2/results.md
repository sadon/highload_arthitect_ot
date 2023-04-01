
# Результаты нагрузочного тестирования

````commandline
curl -X 'GET' \
  'http://localhost:8000/user/search?first_name=%D0%94%D0%BC%D0%B8%D1%82%D1%80&last_name=%D0%92&skip=0&limit=1000' \
  -H 'accept: application/json'
````
Базовый запрос:

Имя/Фамилия: **Дмитр В**
![img.png](img.png)

До создания индексов:
## 1 поток(запрос):
- Latency: ~ 280ms
![latency-1-request-before-index.png](latency-1-request-before-index.png)
- Throughput: 228 rounds/minute
![img_1.png](img_1.png)

## 10 потоков:
- Latency: = 2476ms
- Throughput: 231 rounds/minute
![img_2.png](img_2.png)

## 20 потоков

- Latency: ~ 4800ms
- Throughput: 231 rounds/minute
![img_3.png](img_3.png)
![latency-20-request-before-index.png](latency-20-request-before-index.png)

## Более 20 потоков
- приложению не хватает ресурсов, срабатывают таймауты

# SQL запросы

SELECT *
FROM users
WHERE users.first_name LIKE 'Д%' AND users.second_name LIKE 'В%'
LIMIT 2000;

# Создание индекса

````commandline
CREATE INDEX firstname_lastname
    ON public.users USING btree
    (first_name ASC NULLS LAST, second_name ASC NULLS LAST)
    TABLESPACE pg_default;
````

----

1 апреля
![img_4.png](img_4.png)

![img_5.png](img_5.png)
