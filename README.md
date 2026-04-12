# E-commerce Core

## Описание проекта
Реализация ядра для интернет-магазина в рамках домашнего задания по ООП.

## Реализованный функционал
- Класс `Product` с атрибутами: name, description, price, quantity
- Класс `Category` с атрибутами: name, description, products
- Атрибуты класса `Category`: category_count, product_count
- Автоматический подсчет количества категорий и товаров при инициализации

## Установка и запуск
1. Клонируйте репозиторий
2. Установите Poetry: `pip install poetry`
3. Установите зависимости: `poetry install`
4. Активируйте окружение: `poetry shell`
5. Запустите main.py: `python main.py`

## Тестирование
```bash
pytest --cov=src --cov-report=html