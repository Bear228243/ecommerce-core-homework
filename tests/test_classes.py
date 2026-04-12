import pytest
from src.classes import Product, Category


# Фикстуры для тестов
@pytest.fixture
def sample_product():
    return Product("iPhone 15", "Latest model", 120000.0, 3)


@pytest.fixture
def sample_category(sample_product):
    return Category("Smartphones", "All mobile phones", [sample_product])


# 1. Тест инициализации Product
def test_product_init(sample_product):
    assert sample_product.name == "iPhone 15"
    assert sample_product.description == "Latest model"
    assert sample_product.price == 120000.0
    assert sample_product.quantity == 3


# 2. Тест инициализации Category
def test_category_init(sample_category):
    assert sample_category.name == "Smartphones"
    assert sample_category.description == "All mobile phones"
    assert len(sample_category.products) == 1


def test_category_init_empty_products():
    empty_category = Category("Empty", "No products")
    assert empty_category.name == "Empty"
    assert empty_category.products == []


# 3. Тест подсчета количества продуктов
def test_product_count_auto():
    # Запоминаем текущие счетчики
    initial_product_count = Category.product_count

    # Создаем товары
    prod1 = Product("Товар 1", "Описание 1", 100.0, 2)
    prod2 = Product("Товар 2", "Описание 2", 200.0, 4)

    # Создаем категорию с двумя товарами
    Category("Тестовая категория", "Описание", [prod1, prod2])

    # Проверяем, что счетчик увеличился на 2
    assert Category.product_count == initial_product_count + 2


# 4. Тест подсчета количества категорий
def test_category_count_auto():
    # Запоминаем текущее количество категорий
    initial_category_count = Category.category_count

    # Создаем несколько категорий
    Category("Категория 1", "Описание 1")
    Category("Категория 2", "Описание 2")
    Category("Категория 3", "Описание 3")

    # Проверяем, что счетчик увеличился на 3
    assert Category.category_count == initial_category_count + 3
