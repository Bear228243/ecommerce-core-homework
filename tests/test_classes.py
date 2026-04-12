import pytest
from src.classes import Product, Category


# Фикстуры
@pytest.fixture
def sample_product():
    return Product("iPhone 15", "Latest model", 120000.0, 3)


@pytest.fixture
def sample_products_list():
    return [
        Product("Samsung S24", "256GB, Black", 80000.0, 5),
        Product("iPhone 15", "128GB, Blue", 95000.0, 3),
    ]


@pytest.fixture
def sample_category(sample_products_list):
    return Category("Smartphones", "All mobile phones", sample_products_list)


# 1. Тесты инициализации Product
def test_product_init(sample_product):
    assert sample_product.name == "iPhone 15"
    assert sample_product.description == "Latest model"
    assert sample_product.price == 120000.0
    assert sample_product.quantity == 3


# 2. Тесты инициализации Category
def test_category_init(sample_category):
    assert sample_category.name == "Smartphones"
    assert sample_category.description == "All mobile phones"
    assert len(sample_category.get_products_list()) == 2


def test_category_init_empty_products():
    empty_category = Category("Empty", "No products")
    assert empty_category.name == "Empty"
    assert empty_category.get_products_list() == []


# 3. Тесты подсчета количества продуктов
def test_product_count_auto():
    initial_product_count = Category.product_count

    prod1 = Product("Товар 1", "Описание 1", 100.0, 2)
    prod2 = Product("Товар 2", "Описание 2", 200.0, 4)
    Category("Тестовая категория", "Описание", [prod1, prod2])

    assert Category.product_count == initial_product_count + 2


# 4. Тесты подсчета количества категорий
def test_category_count_auto():
    initial_category_count = Category.category_count

    Category("Категория 1", "Описание 1")
    Category("Категория 2", "Описание 2")
    Category("Категория 3", "Описание 3")

    assert Category.category_count == initial_category_count + 3


# 5. Тест метода add_product
def test_add_product():
    category = Category("Test", "Description")
    initial_count = Category.product_count

    new_product = Product("New Phone", "Desc", 50000.0, 2)
    category.add_product(new_product)

    assert len(category.get_products_list()) == 1
    assert Category.product_count == initial_count + 1


# 6. Тест геттера products
def test_products_getter(sample_products_list):
    category = Category("Test", "Desc", sample_products_list)
    expected_output = (
        "Samsung S24, 80000.0 руб. Остаток: 5 шт.\n"
        "iPhone 15, 95000.0 руб. Остаток: 3 шт."
    )
    assert category.products == expected_output


def test_products_getter_empty():
    category = Category("Empty", "No products")
    assert category.products == "В категории нет товаров."


# 7. Тест класс-метода new_product
def test_new_product_classmethod():
    product_data = {
        "name": "Xiaomi 13",
        "description": "512GB, White",
        "price": 65000.0,
        "quantity": 7
    }
    product = Product.new_product(product_data)

    assert product.name == "Xiaomi 13"
    assert product.description == "512GB, White"
    assert product.price == 65000.0
    assert product.quantity == 7


# 8. Тесты геттера и сеттера цены
def test_price_getter(sample_product):
    assert sample_product.price == 120000.0


def test_price_setter_positive(sample_product):
    sample_product.price = 130000.0
    assert sample_product.price == 130000.0


def test_price_setter_zero(capsys):
    product = Product("Test", "Desc", 100.0, 1)
    product.price = 0
    captured = capsys.readouterr()
    assert product.price == 100.0
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_price_setter_negative(capsys):
    product = Product("Test", "Desc", 100.0, 1)
    product.price = -50
    captured = capsys.readouterr()
    assert product.price == 100.0
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


# 9. Тест приватности атрибута __products
def test_products_is_private(sample_category):
    with pytest.raises(AttributeError):
        _ = sample_category.__products


# 10. Тест метода __str__ для Product
def test_product_str():
    product = Product("Test Product", "Description", 100.0, 5)
    assert str(product) == "Test Product, 100.0 руб. Остаток: 5 шт."


def test_product_str_with_float_price():
    product = Product("Test", "Desc", 99.99, 3)
    assert str(product) == "Test, 99.99 руб. Остаток: 3 шт."


# 11. Тест метода __str__ для Category
def test_category_str(sample_products_list):
    category = Category("Smartphones", "Description", sample_products_list)
    # Samsung: 5 шт, iPhone: 3 шт = всего 8
    assert str(category) == "Smartphones, количество продуктов: 8 шт."


def test_category_str_empty():
    category = Category("Empty", "No products")
    assert str(category) == "Empty, количество продуктов: 0 шт."


def test_category_str_single_product():
    product = Product("Single", "Desc", 100.0, 10)
    category = Category("Test", "Desc", [product])
    assert str(category) == "Test, количество продуктов: 10 шт."


# 12. Тест метода __add__ для Product
def test_product_add():
    product1 = Product("Product 1", "Desc", 100.0, 5)  # 500
    product2 = Product("Product 2", "Desc", 200.0, 3)  # 600
    result = product1 + product2
    assert result == 1100.0


def test_product_add_different_quantities():
    product1 = Product("P1", "D1", 50.0, 10)   # 500
    product2 = Product("P2", "D2", 100.0, 1)   # 100
    result = product1 + product2
    assert result == 600.0


def test_product_add_with_float():
    product1 = Product("P1", "D1", 99.99, 2)   # 199.98
    product2 = Product("P2", "D2", 50.50, 1)   # 50.50
    result = product1 + product2
    assert result == 250.48


def test_product_add_type_error():
    product = Product("Test", "Desc", 100.0, 1)
    with pytest.raises(TypeError):
        _ = product + "not a product"
