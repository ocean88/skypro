# Skypro

## Описание

Аттестационное задание №2, приложение, в котором пользователи могут писать посты и комментировать их.

## Установка и запуск проекта

### 1. Клонирование репозитория

Сначала клонируйте репозиторий на ваш локальный компьютер:

```bash
git clone https://github.com/ваш-репозиторий.git

- Создайте виртуальное окружение:
python -m venv env

- Активируйте виртуальное окружение:
.\env\Scripts\activate

- .env_sample переименовать .env и указать свои настройки
DJANGO_SECRET_KEY = YOUR_DJANGO_KEY
POSTGRES_DB = YOUR_DB_NAME
POSTGRES_USER = YOUR_DB_LOGIN
POSTGRES_PASSWORD = YOUR_DB_PASSWORD

- установить все зависимости pip install -r requirements.txt
- применить миграции и создать пользователя python manage.py migrate
- также для создания пользователя использовались команды cu и csu соотвественно. 
- Запуск проекта python manage.py runserver


