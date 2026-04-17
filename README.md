# Coffee Shop API (DigitalHub v2)

REST API для автоматизации заказов в кофейне.

## Функционал
* Создание и просмотр заказов (доступно всем).
* Изменение статуса заказа (Принят/Закрыт) — **только для автора заказа**.
* Автоматическая документация Swagger.

## Технологии
* Python 3.13
* Django 6.0
* Django REST Framework
* drf-yasg (Swagger)

## Как запустить проект локально
1. Клонировать репозиторий.
2. Создать и активировать `venv`.
3. Установить зависимости: `pip install django djangorestframework drf-yasg`.
4. Применить миграции: `python manage.py migrate`.
5. Запустить сервер: `python manage.py runserver`.

## Документация
После запуска доступна по адресу: `http://127.0.0.1:8000/swagger/`