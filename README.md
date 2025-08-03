# ITK Academy Test Exercise

Проект на Django с PostgreSQL в Docker-контейнерах

## 📋 Требования
- Docker 20.10+
- Docker Compose 2.0+
- Python 3.10+ (только для локальной разработки)

## 🚀 Быстрый старт

### 1. Клонирование репозитория

    git clone https://github.com/your-username/ITK-Academy-test-exercise.git
    cd ITK-Academy-test-exercise

### 2. Настройка окружения

Скопируйте файл .env_example и замените значения переменных на свои

    cp .env_example .env

### 3. Запустите проект командой

    docker-compose up -d --build

### 4. Примините миграции

    docker-compose exec web python manage.py migrate

### 5. Создайте супер пользователя

    docker-compose exec web python manage.py createsuperuser

## Запуск тестов
    
Запуск тестов производится командой:

    docker-compose exec web python manage.py test