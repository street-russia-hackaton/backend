# Street Russia Hackathon Project

## Оглавление <a id="contents"></a>

1. [О проекте](#about)
2. [Авторы проекта](#authors)
3. [Стек технологий](#tools)
4. [Установка](#installation)
5. [Запуск](#start)


## О проекте <a id="about"></a>

События и мероприятия уличных дисциплин по всем направлениям.


## Авторы проекта <a id="authors"></a>

Команда:

- Backend
  - [Бобков Константин](https://github.com/deltabobkov) (TG [@Bi_oKey](https://t.me/Bi_oKey))
  - [Роман Буров](https://github.com/rvburov) (TG [@romanburov89](https://t.me/romanburov89))
 
## Стек технологий <a id="tools"></a>

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-green)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/DRF-3.15.1-orange)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-blue)](https://www.postgresql.org/)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

## Установка зависимостей для локального разворачивания проекта<a id="installation"></a>

1. Склонируйте репозиторий:

  ```
    git@github.com:street-russia-hackaton/backend.git
    cd backend
  ```

  2. В корневой директории создайте .env файл:
  ```
    cd backend
    touch .env
  ```

3. Заполните по примеру своими значениями:
.env.example

## Запуск <a id="start"></a>

Выполните миграции:
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```

Создайте суперпользователя:
  ```
    python manage.py createsuperuser
  ```

Запустите проект следующей командой:
  ```
   manage.py runserver
  ```

Зайти в админ-панель:
[Admin](http://127.0.0.1:8000/admin/)
