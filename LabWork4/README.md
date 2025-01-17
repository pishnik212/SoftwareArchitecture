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
    + [Операции с аккаунтами абитуриентов](#title2)
    + [Операции с заявками абитуриентов](#title2)
* [Тестирование API](#title1_2)
    + [Операции с аккаунтами пользователей](#title2_2)
      - [POST user](#title3_1_1)
      - [GET user by id](#title3_2_1)
      - [PUT user by id](#title3_3_1)
      - [DELETE user by id](#title3_4_1)

## Диаграмма компонентов
Диграмма компонентов для сервиса работы со списками абитуриентов:
## <a id="title1_1">Документация по API</a>

### <a id="title2_1">Операции с аккаунтами пользователей</a>

### <a id="title3_1">POST user </a>

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
### <a id="title3_2">GET user by id</a>

**Описание:** Операция получения данных о пользователе системы

**Входные данные:** 
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


## <a id="title1_2">Тестирование API</a>

### <a id="title2_2">Операции с аккаунтами пользователей</a>

### <a id="title3_1_1">POST user </a>

Authorization 

 <img width="800" src="Lab4_Images/Auth.png" alt="1"/>
 <img width="800" src="Lab4_Images/token.png" alt="1"/>

Body

 <img width="800" src="Lab4_Images/post_user_0.png" alt="1"/>

Headres

 <img width="800" src="Lab4_Images/post_user_1.png" alt="1"/>

Tests

<img width="800" src="Lab4_Images/post_user_2.png" alt="1"/>

### <a id="title3_2_1">GET user by id</a>

Authorization 

 <img width="800" src="Lab4_Images/get_user_auth.png" alt="1"/>

Body

 <img width="800" src="Lab4_Images/get_user_body.png" alt="1"/>

Headres

 <img width="800" src="Lab4_Images/get_user_headers.png" alt="1"/>

Tests

<img width="800" src="Lab4_Images/get_user_test.png" alt="1"/>
