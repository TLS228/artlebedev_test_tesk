#!/bin/bash
echo "Выполняем миграции..."
python manage.py migrate

echo "Парсим данные..."
python manage.py parse_data

echo "Запускаем сервер..."
gunicorn cultural_api.wsgi:application --bind 0.0.0.0:8000