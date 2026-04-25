import pytest
from src.classes import Product, Category, Smartphone, LawnGrass


# Фикстуры
@pytest.fixture
def sample_product():
    return Product("iPhone 15", "Latest model", 120000.0, 3)


@pytest.fixture
def sample_smartphone():
    return Smartphone(
        name="Samsung S24",
        description="256GB, Black",
        price=80000.0,
        quantity=5,
        efficiency=9.5,
        model="S24",
        memory=256,
        color="Black"
    )


@pytest.fixture
def sample_lawn_grass():
    return LawnGrass(
        name="Green Grass",
        description="Газонная трава",
        price=500.0,
        quantity=100,
        country="Россия",
        germination_period=14,
        color="Зеленый"
    )


@pytest.fixture
def sample_products_list():
    return [
        Product("Generic Product", "Description", 1000.0, 2),
        Smartphone("Xiaomi 13", "512GB", 65000.0, 3, 9.0, "13", 512, "White"),
        LawnGrass("Lawn", "Grass", 300.0, 50, "USA", 10, "Green"),
    ]


@pytest.fixture
def sample_category(sample_products_list):
    return Category("Mixed Category", "All types of products", sample_products_list)


# 1. Тесты инициализации Product
def test_product_init(sample_product):
    assert sample_product.name == "iPhone 15"
    assert sample_product.description == "Latest model"
    assert sample_product.price == 120000.0
    assert sample_product.quantity == 3


# 2. Тесты инициализации Smartphone
def test_smartphone_init(sample_smartphone):
    assert sample_smartphone.name == "Samsung S24"
    assert sample_smartphone.description == "256GB, Black"
    assert sample_smartphone.price == 80000.0
    assert sample_smartphone.quantity == 5
    assert sample_smartphone.efficiency == 9.5
    assert sample_smartphone.model == "S24"
    assert sample_smartphone.memory == 256
    assert sample_smartphone.color == "Black"


# 3. Тесты инициализации LawnGrass
def test_lawn_grass_init(sample_lawn_grass):
    assert sample_lawn_grass.name == "Green Grass"
    assert sample_lawn_grass.description == "Газонная трава"
    assert sample_lawn_grass.price == 500.0
    assert sample_lawn_grass.quantity == 100
    assert sample_lawn_grass.country == "Россия"
    assert sample_lawn_grass.germination_period == 14
    assert sample_lawn_grass.color == "Зеленый"


# 4. Проверка наследования
def test_smartphone_is_product_subclass():
    assert issubclass(Smartphone, Product)


def test_lawn_grass_is_product_subclass():
    assert issubclass(LawnGrass, Product)


def test_smartphone_is_product_instance(sample_smartphone):
    assert isinstance(sample_smartphone, Product)


def test_lawn_grass_is_product_instance(sample_lawn_grass):
    assert isinstance(sample_lawn_grass, Product)


# 5. Тесты инициализации Category
def test_category_init(sample_category):
    assert sample_category.name == "Mixed Category"
    assert sample_category.description == "All types of products"
    assert len(sample_category.get_products_list()) == 3


# 6. Тесты подсчета количества продуктов и категорий
def test_product_count_auto():
    initial_product_count = Category.product_count

    prod1 = Product("Товар 1", "Описание 1", 100.0, 2)
    prod2 = Smartphone("Phone", "Desc", 50000.0, 1, 8.0, "M1", 128, "Blue")
    Category("Тестовая категория", "Описание", [prod1, prod2])

    assert Category.product_count == initial_product_count + 2


def test_category_count_auto():
    initial_category_count = Category.category_count

    Category("Категория 1", "Описание 1")
    Category("Категория 2", "Описание 2")

    assert Category.category_count == initial_category_count + 2


# 7. Тест метода add_product с проверкой типа
def test_add_product_valid(sample_category, sample_smartphone):
    initial_count = Category.product_count
    initial_len = len(sample_category.get_products_list())

    sample_category.add_product(sample_smartphone)

    assert len(sample_category.get_products_list()) == initial_len + 1
    assert Category.product_count == initial_count + 1


def test_add_product_invalid_type():
    category = Category("Test", "Description")
    with pytest.raises(TypeError) as exc_info:
        category.add_product("not a product")
    assert "В категорию можно добавлять только объекты Product или его наследников" in str(exc_info.value)


def test_add_product_invalid_dict():
    category = Category("Test", "Description")
    with pytest.raises(TypeError):
        category.add_product({"name": "test"})


# 8. Тест геттера products
def test_products_getter(sample_products_list):
    category = Category("Test", "Desc", sample_products_list)
    products_str = category.products
    assert "Generic Product" in products_str
    assert "Xiaomi 13" in products_str
    assert "Lawn" in products_str


# 9. Тест класс-метода new_product
def test_new_product_classmethod():
    product_data = {
        "name": "Test Product",
        "description": "Test Desc",
        "price": 1000.0,
        "quantity": 5
    }
    product = Product.new_product(product_data)

    assert product.name == "Test Product"
    assert product.price == 1000.0
    assert product.quantity == 5


# 10. Тесты геттера и сеттера цены
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


# 11. Тест метода __str__
def test_product_str(sample_product):
    assert str(sample_product) == "iPhone 15, 120000.0 руб. Остаток: 3 шт."


def test_smartphone_str(sample_smartphone):
    assert str(sample_smartphone) == "Samsung S24, 80000.0 руб. Остаток: 5 шт."


def test_lawn_grass_str(sample_lawn_grass):
    assert str(sample_lawn_grass) == "Green Grass, 500.0 руб. Остаток: 100 шт."


def test_category_str(sample_products_list):
    category = Category("Test", "Desc", sample_products_list)
    # Product: 2 + Smartphone: 3 + LawnGrass: 50 = 55
    assert str(category) == "Test, количество продуктов: 55 шт."


# 12. Тест метода __add__
def test_product_add_same_type():
    product1 = Product("P1", "D1", 100.0, 5)  # 500
    product2 = Product("P2", "D2", 200.0, 3)  # 600
    assert product1 + product2 == 1100.0


def test_smartphone_add_same_type():
    phone1 = Smartphone("P1", "D1", 1000.0, 2, 9.0, "M1", 128, "Black")  # 2000
    phone2 = Smartphone("P2", "D2", 2000.0, 1, 9.5, "M2", 256, "White")  # 2000
    assert phone1 + phone2 == 4000.0


def test_lawn_grass_add_same_type():
    grass1 = LawnGrass("G1", "D1", 100.0, 10, "RU", 7, "Green")  # 1000
    grass2 = LawnGrass("G2", "D2", 200.0, 5, "USA", 14, "Dark Green")  # 1000
    assert grass1 + grass2 == 2000.0


def test_add_different_types_raises_error(sample_smartphone, sample_lawn_grass):
    with pytest.raises(TypeError) as exc_info:
        _ = sample_smartphone + sample_lawn_grass
    assert "Нельзя складывать товары разных классов" in str(exc_info.value)


def test_add_product_with_smartphone_raises_error(sample_product, sample_smartphone):
    with pytest.raises(TypeError) as exc_info:
        _ = sample_product + sample_smartphone
    assert "Нельзя складывать товары разных классов" in str(exc_info.value)


def test_add_smartphone_with_lawn_grass_raises_error(sample_smartphone, sample_lawn_grass):
    with pytest.raises(TypeError):
        _ = sample_smartphone + sample_lawn_grass


# 13. Тест приватности атрибута __products
def test_products_is_private(sample_category):
    with pytest.raises(AttributeError):
        _ = sample_category.__products
