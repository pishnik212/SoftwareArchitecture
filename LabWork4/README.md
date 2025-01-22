# Лабораторная работа №4

**Тема:** Проектирование REST API

**Цель работы:** Получить опыт проектирования программного интерфейса.

## Документация по API
* [Документация по API](#title1_1)
    + [Операции с аккаунтами пользователей](#title2_1)
      - [POST user](#title3_1)
      - [GET user by id](#title3_2)
      - [PUT user by id](#title3_3)
      - [DELETE user by id](#title3_4)
    + [Операции с абитуриентами](#title2_3)
      - [POST entrant](#title3_5)
      - [GET entrant by id](#title3_6)
      - [PUT entrant by id](#title3_7)
      - [DELETE entrant by id](#title3_8)
    + [Операции с заявками абитуриентов](#title2_5)
      - [POST application](#title3_9)
      - [GET application by id](#title3_10)
      - [PUT application by id](#title3_11)
      - [DELETE application by id](#title3_12)
* [Тестирование API](#title1_2)
    + [Операции с аккаунтами пользователей](#title2_2)
      - [POST user](#title3_1_1)
      - [GET user by id](#title3_2_1)
      - [PUT user by id](#title3_3_1)
      - [DELETE user by id](#title3_4_1)
    + [Операции с абитуриентами](#title2_4)
      - [POST entrant](#title3_5_1)
      - [GET entrant by id](#title3_6_1)
      - [PUT entrant by id](#title3_7_1)
      - [DELETE entrant by id](#title3_8_1)
    + [Операции с заявками абитуриентов](#title2_6)
      - [POST application](#title3_9_1)
      - [GET application by id](#title3_10_1)
      - [PUT application by id](#title3_11_1)
      - [DELETE application by id](#title3_12_1)
        

## <a id="title1_1">Документация по API</a>

### <a id="title2_1">Операции с аккаунтами пользователей</a>

### <a id="title3_1">POST / user / </a>

**Описание:** Операция добавления пользователя в систему

**Входные данные:** Body в json-формате
* username (строка) - Имя пользователя
* password (строка) - Пароль пользователя
* role_id (целочисленное) - Идентификатор роли пользователя в системе

**Пример входных данных:** 
```json
{
  "username": "test_user",
  "password": "my_password_035",
  "role_id": 1
}
```

**Пример выходных данных:** 
```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJteV9wYXNzd29yZF8wMzUiLCJleHAiOjYxNzM3MDkyODAxfQ.C2TK7OvffDBfh7U1A2-tSN1EeojZbvyKsDUHUZdLTvU",
    "user_id": 1,
    "username": "test_user",
    "password": "my_password_035",
    "role_id": 1
}
```

**cURL:**
```
curl --location 'http://127.0.0.1:8000/user' \
--header 'Content-Type: application/json' \
--header 'Authorization: ••••••' \
--data '{
  "username": "test_user",
  "password": "my_password_035",
  "role_id": 1
}
'
```
### <a id="title3_2">GET / user / {id}</a>

**Описание:** Операция получения данных о пользователе системы

**Входные данные:** Query
* id (целое число) - Идентификатор искомого пользователя в системе

**Пример входных данных:** 
```
/user/1
```

**Пример выходных данных:** 
```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJteV9wYXNzd29yZF8wMzUiLCJleHAiOjYxNzM3MDkyODAxfQ.C2TK7OvffDBfh7U1A2-tSN1EeojZbvyKsDUHUZdLTvU",
    "user_id": 1,
    "username": "test_user",
    "password": "my_password_035",
    "role_id": 1
}
```

**cURL:**
```
curl --location 'http://127.0.0.1:8000/user/1' \
--header 'Authorization: ••••••'
```


### <a id="title3_3">PUT / user / {id}</a>

**Описание:** Операция обновления данных пользователя системы

**Входные данные:** Query
* id (целое число) - Идентификатор искомого пользователя в системе

Body в json-формате
* username (строка) - Имя пользователя
* password (строка) - Пароль пользователя
* role_id (целочисленное) - Идентификатор роли пользователя в системе

**Пример входных данных:** 
```
/user/1
```

```json
{
  "username": "test_user",
  "password": "my_new_password_077",
  "role_id": 1
}
```

**Пример выходных данных:** 
```json
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJteV9wYXNzd29yZF8wMzUiLCJleHAiOjYxNzM3MDkyODAxfQ.C2TK7OvffDBfh7U1A2-tSN1EeojZbvyKsDUHUZdLTvU",
    "user_id": 1,
    "username": "test_user",
    "password": "my_new_password_077",
    "role_id": 1
}
```

**cURL:**
```
curl --location --request PUT 'http://127.0.0.1:8000/user/1' \
--header 'Content-Type: application/json' \
--header 'Authorization: ••••••' \
--data '{
  "username": "test_user",
  "password": "my_new_password_077",
  "role_id": 1
}'
```

### <a id="title3_4">DELETE / user / {id}</a>

**Описание:** Операция удаления пользователя из системы

**Входные данные:** Query
* id (целое число) - Идентификатор пользователя для удаления
  

**Пример входных данных:** 
```
/user/1
```


**Пример выходных данных:** 
Выходных данных нет, необходимо смотреть на статус выполнения запроса.

**cURL:**
```
curl --location --request DELETE 'http://127.0.0.1:8000/user/1' \
--header 'Authorization: ••••••'
```

### <a id="title2_3">Операции с абитуриентами</a>

### <a id="title3_5">POST / entrant / </a>

**Описание:** Операция добавления сведений об абитуриенте в систему

**Входные данные:** Body в json-формате
* firstName (строка) - Имя абитуриента
* lastName (строка) - Фамилия абитуриента
* snils (строка) - СНИЛС абитуриента

**Пример входных данных:** 
```json
{
  "firstName": "Анна",
  "lastName": "Бокалова",
  "snils": "333-333-333 13"
}
```

**Пример выходных данных:** 
```json
{
    "id": 3,
    "firstName": "Анна",
    "lastName": "Вычетаева",
    "snils": "333-333-333 53"
}
```

**cURL:**
```
curl --location 'http://127.0.0.1:8000/    entrant' \--header 'Content-Type: application/json' \--header 'Authorization: ••••••' \--data '{  "firstName": "Анна",  "lastName": "Вычетаева",  "snils": "333-333-333 53"}'
```

### <a id="title3_6">GET / user / {id}</a>

**Описание:** Операция получения данных об абитуриенте по его id

**Входные данные:** Query
* id (целое число) - Идентификатор искомого абитуриента в системе

**Пример входных данных:** 
```
/entrant/1
```

**Пример выходных данных:** 
```json
{
    "id": 1,
    "firstName": "Анна",
    "lastName": "Бокалова",
    "snils": "333-333-333 13"
}
```

**cURL:**
```
curl --location 'http://127.0.0.1:8000/entrant/1' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzZWN1cmVwYXNzd29yZDEyMyIsImV4cCI6NjE3MzcwMjAwMTl9.9bObIcu5JeW3Jr9F3ZF2YyDPKO2kioSYQlRCxpxAG4A'
```


### <a id="title3_7">PUT / entrant / {id}</a>

**Описание:** Операция обновления данных абитуриента в системе

**Входные данные:** Query
* id (целое число) - Идентификатор искомого абитуриента в системе

Body в json-формате
* firstName (строка) - Имя абитуриента
* lastName (строка) - Фамилия абитуриента
* snils (строка) - СНИЛС абитуриента

**Пример входных данных:** 
```
/entrant/1
```

```json
{
  "firstName": "Анна",
  "lastName": "Вычетаева",
  "snils": "333-333-333 77"
}
```

**Пример выходных данных:** 
```json
{
    "id": 1,
    "firstName": "Анна",
    "lastName": "Вычетаева",
    "snils": "333-333-333 77"
}
```

**cURL:**
```
curl --location --request PUT 'http://127.0.0.1:8000/entrant/1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzZWN1cmVwYXNzd29yZDEyMyIsImV4cCI6NjE3MzcwMjAwMTl9.9bObIcu5JeW3Jr9F3ZF2YyDPKO2kioSYQlRCxpxAG4A' \
--data '{
  "firstName": "Анна",
  "lastName": "Вычетаева",
  "snils": "333-333-333 77"
}'
```

### <a id="title3_8">DELETE / entrant / {id}</a>

**Описание:** Операция удаления данных об абитуриенте из системы

**Входные данные:** Query
* id (целое число) - Идентификатор абитуриента для удаления
  

**Пример входных данных:** 
```
/entrant/1
```


**Пример выходных данных:** 
Выходных данных нет, необходимо смотреть на статус выполнения запроса.

**cURL:**
```
curl --location --request DELETE 'http://127.0.0.1:8000/user/1' \
--header 'Authorization: ••••••'
```


### <a id="title2_5">Операции с заявками абитуриентов</a>

### <a id="title3_9">POST / application / </a>

**Описание:** Операция добавления сведений о заявках абитуриентов

**Входные данные:** Body в json-формате
* submissionDT (дата и время) - Дата подачи заявки абитуриентом
* status (строка) - Статус заявки
* entrant (Абитуриент) - Сведения автора заявки - абитуриента (id - идентификатор, firstName - имя, lastName - фамилия, snils - СНИЛС)

**Пример входных данных:** 
```json
{
  "submissionDT": "2024-12-01 11:15",
  "status": "Создана",
  "entrant": [{
            "firstName": "Анна",
            "lastName": "Бокалова",
            "snils": "333-333-333 13"
            }]
}

```

**Пример выходных данных:** 
```json
{
    "id": 1,
    "submissionDT": "2024-12-01 11:15",
    "status": "Создана",
    "entrant": [
        {
            "id": 1,
            "firstName": "Анна",
            "lastName": "Бокалова",
            "snils": "333-333-333 13"
        }
    ]
}
```

**cURL:**
```
curl --location 'http://127.0.0.1:8000/application/' \
--header 'Content-Type: application/json' \
--header 'Authorization: ••••••' \
--data '{
  "submissionDT": "2024-12-01 11:15",
  "status": "Создана",
  "entrant": [{
            "firstName": "Анна",
            "lastName": "Бокалова",
            "snils": "333-333-333 13"
            }]
}
'
```

### <a id="title3_10">GET / application / {id}</a>

**Описание:** Операция получения данных о заявке абитуриента по ее id 

**Входные данные:** Query
* id (целое число) - Идентификатор искомой заявки абитуриента в системе

**Пример входных данных:** 
```
/application/5
```

**Пример выходных данных:** 
```json
{
    "id": 5,
    "submissionDT": "2024-12-01 11:15",
    "status": "Выполнена",
    "entrant": [
        {
            "id": 1,
            "firstName": "Анна",
            "lastName": "Бокалова",
            "snils": "333-333-333 13"
        }
    ]
}
```

**cURL:**
```
curl --location 'http://127.0.0.1:8000/application/5' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzZWN1cmVwYXNzd29yZDEyMyIsImV4cCI6NjE3MzcwMjAwMTl9.9bObIcu5JeW3Jr9F3ZF2YyDPKO2kioSYQlRCxpxAG4A'
```


### <a id="title3_11">PUT / application / {id}</a>

**Описание:** Операция обновления данных абитуриента в системе

**Входные данные:** Query
* id (целое число) - Идентификатор редактируемой заявки в системе

Body в json-формате
* submissionDT (дата и время) - Дата подачи заявки абитуриентом
* status (строка) - Статус заявки
* entrant (Абитуриент) - Сведения автора заявки - абитуриента (id - идентификатор, firstName - имя, lastName - фамилия, snils - СНИЛС)

**Пример входных данных:** 
```
/application/5
```

```json
{
  "submissionDT": "2024-12-01 11:15",
  "status": "Выполнена",
  "entrant": [{
            "firstName": "Анна",
            "lastName": "Бокалова",
            "snils": "333-333-333 13"
            }]
}
```

**Пример выходных данных:** 
```json
{
    "id": 5,
    "submissionDT": "2024-12-01 11:15",
    "status": "Выполнена",
    "entrant": [
        {
            "id": 1,
            "firstName": "Анна",
            "lastName": "Бокалова",
            "snils": "333-333-333 13"
        }
    ]
}
```

**cURL:**
```
curl --location --request PUT 'http://127.0.0.1:8000/application/5' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzZWN1cmVwYXNzd29yZDEyMyIsImV4cCI6NjE3MzcwMjAwMTl9.9bObIcu5JeW3Jr9F3ZF2YyDPKO2kioSYQlRCxpxAG4A' \
--data '{
  "submissionDT": "2024-12-01 11:15",
  "status": "Выполнена",
  "entrant": [{
            "firstName": "Анна",
            "lastName": "Бокалова",
            "snils": "333-333-333 13"
            }]
}

'
```

### <a id="title3_12">DELETE / application / {id}</a>

**Описание:** Операция удаления заявки абитуриента из системы

**Входные данные:** Query
* id (целое число) - Идентификатор заявки для удаления
  

**Пример входных данных:** 
```
/application/5
```


**Пример выходных данных:** 
Выходных данных нет, необходимо смотреть на статус выполнения запроса.

**cURL:**
```
curl --location --request DELETE 'http://127.0.0.1:8000/application/5' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzZWN1cmVwYXNzd29yZDEyMyIsImV4cCI6NjE3MzcwMjAwMTl9.9bObIcu5JeW3Jr9F3ZF2YyDPKO2kioSYQlRCxpxAG4A'
```















## <a id="title1_2">Тестирование API</a>

### <a id="title2_2">Операции с аккаунтами пользователей</a>

### <a id="title3_1_1">POST user </a>

Authorization 

 <img width="800" src="Lab4_Images/Auth.png" alt="1"/>
 <img width="800" src="Lab4_Images/token.png" alt="1"/>

Body

 <img width="800" src="Lab4_Images/post_user_0.png" alt="1"/>

Headers

 <img width="800" src="Lab4_Images/post_user_1.png" alt="1"/>

Tests

<img width="800" src="Lab4_Images/post_user_2.png" alt="1"/>

### <a id="title3_2_1">GET user by id</a>

Authorization 

 <img width="800" src="Lab4_Images/get_user_auth.png" alt="1"/>

Body

 <img width="800" src="Lab4_Images/get_user_body.png" alt="1"/>

Headers

 <img width="800" src="Lab4_Images/get_user_headers.png" alt="1"/>

Tests

<img width="800" src="Lab4_Images/get_user_test.png" alt="1"/>

### <a id="title3_3_1">PUT user by id</a>

Body

 <img width="800" src="Lab4_Images/put_user_body.png" alt="1"/>

Headers

 <img width="800" src="Lab4_Images/put_user_headers.png" alt="1"/>

Tests

<img width="800" src="Lab4_Images/put_user_test.png" alt="1"/>

### <a id="title3_4_1">DELETE user by id</a>

Body

 <img width="800" src="Lab4_Images/delete_user_body.png" alt="1"/>

Headers

 <img width="800" src="Lab4_Images/delete_user_headers.png" alt="1"/>

Tests

<img width="800" src="Lab4_Images/delete_user_test.png" alt="1"/>

### <a id="title2_4">Операции с данными абитуриентов</a>

### <a id="title3_5_1">POST entrant by id</a>

Authorization

 <img width="800" src="Lab4_Images/post_entrant_auth.png" alt="1"/>

Body

 <img width="800" src="Lab4_Images/post_entrant_body.png" alt="1"/>

Headers

 <img width="800" src="Lab4_Images/post_entrant_headers.png" alt="1"/>

Tests

<img width="800" src="Lab4_Images/post_entrant_test.png" alt="1"/>

### <a id="title3_6_1">GET entrant by id</a>


Body

 <img width="800" src="Lab4_Images/get_entrant_body.png" alt="1"/>

Headers

 <img width="800" src="Lab4_Images/get_entrant_headers.png" alt="1"/>

Tests

<img width="800" src="Lab4_Images/get_entrant_test.png" alt="1"/>

### <a id="title3_7_1">PUT entrant by id</a>

Body

 <img width="800" src="Lab4_Images/put_entrant_body.png" alt="1"/>

Headers

 <img width="800" src="Lab4_Images/put_entrant_headers.png" alt="1"/>

Tests

<img width="800" src="Lab4_Images/put_entrant_test.png" alt="1"/>

### <a id="title3_8_1">DELETE entrant by id</a>

Body

 <img width="800" src="Lab4_Images/delete_entrant_body.png" alt="1"/>

Headers

 <img width="800" src="Lab4_Images/delete_entrant_headers.png" alt="1"/>

Tests

<img width="800" src="Lab4_Images/delete_entrant_test.png" alt="1"/>


### <a id="title2_6">Операции с заявками абитуриентов</a>

### <a id="title3_9_1">POST application by id</a>
Authorization

 <img width="800" src="Lab4_Images/post_app_auth.png" alt="1"/>

Body

 <img width="800" src="Lab4_Images/post_app_body.png" alt="1"/>

Headers

 <img width="800" src="Lab4_Images/post_app_headers.png" alt="1"/>

Tests

<img width="800" src="Lab4_Images/post_app_test.png" alt="1"/>

### <a id="title3_10_1">GET application by id</a>


Body

 <img width="800" src="Lab4_Images/get_app_body.png" alt="1"/>

Headers

 <img width="800" src="Lab4_Images/get_app_headers.png" alt="1"/>

Tests

<img width="800" src="Lab4_Images/get_app_test.png" alt="1"/>

### <a id="title3_11_1">PUT application by id</a>

Body

 <img width="800" src="Lab4_Images/put_app_body.png" alt="1"/>

Headers

 <img width="800" src="Lab4_Images/put_app_headers.png" alt="1"/>

Tests

<img width="800" src="Lab4_Images/put_app_test.png" alt="1"/>

### <a id="title3_12_1">DELETE application by id</a>

Body

 <img width="800" src="Lab4_Images/delete_app_body.png" alt="1"/>

Headers

 <img width="800" src="Lab4_Images/delete_app_headers.png" alt="1"/>

Tests

<img width="800" src="Lab4_Images/delete_app_test.png" alt="1"/>
