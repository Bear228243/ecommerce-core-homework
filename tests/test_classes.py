import pytest
from src.classes import Product, Category, Smartphone, LawnGrass, BaseProduct, MixinLogger


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


# 1. Тест исключения при нулевом количестве
def test_product_zero_quantity_raises_error():
    """Проверяем, что создание продукта с quantity=0 вызывает ValueError."""
    with pytest.raises(ValueError) as exc_info:
        Product("Test", "Desc", 100.0, 0)
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"


def test_product_negative_quantity_raises_error():
    """Проверяем, что создание продукта с quantity<0 вызывает ValueError."""
    with pytest.raises(ValueError) as exc_info:
        Product("Test", "Desc", 100.0, -5)
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"


def test_product_positive_quantity_works():
    """Проверяем, что продукт с quantity>0 создается нормально."""
    product = Product("Test", "Desc", 100.0, 1)
    assert product.quantity == 1


def test_smartphone_zero_quantity_raises_error():
    """Проверяем, что смартфон с quantity=0 вызывает ValueError."""
    with pytest.raises(ValueError) as exc_info:
        Smartphone("Test", "Desc", 1000.0, 0, 9.0, "Model", 128, "Black")
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"


def test_lawn_grass_zero_quantity_raises_error():
    """Проверяем, что трава с quantity=0 вызывает ValueError."""
    with pytest.raises(ValueError) as exc_info:
        LawnGrass("Test", "Desc", 100.0, 0, "RU", 7, "Green")
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"


# 2. Тесты метода average_price
def test_average_price_with_products(sample_products_list):
    """Проверяем подсчет среднего ценника с товарами."""
    category = Category("Test", "Desc", sample_products_list)
    # Product: 1000.0, Smartphone: 65000.0, LawnGrass: 300.0
    # Среднее = (1000 + 65000 + 300) / 3 = 66300 / 3 = 22100.0
    assert category.average_price() == 22100.0


def test_average_price_single_product():
    """Проверяем средний ценник с одним товаром."""
    product = Product("Test", "Desc", 500.0, 10)
    category = Category("Test", "Desc", [product])
    assert category.average_price() == 500.0


def test_average_price_empty_category():
    """Проверяем, что для пустой категории возвращается 0."""
    category = Category("Empty", "No products")
    assert category.average_price() == 0.0


def test_average_price_multiple_same_price():
    """Проверяем средний ценник с одинаковыми ценами."""
    p1 = Product("P1", "D1", 100.0, 1)
    p2 = Product("P2", "D2", 100.0, 1)
    p3 = Product("P3", "D3", 100.0, 1)
    category = Category("Test", "Desc", [p1, p2, p3])
    assert category.average_price() == 100.0


def test_average_price_after_adding_product():
    """Проверяем пересчет среднего после добавления товара."""
    p1 = Product("P1", "D1", 100.0, 1)
    p2 = Product("P2", "D2", 200.0, 1)
    category = Category("Test", "Desc", [p1])
    assert category.average_price() == 100.0

    category.add_product(p2)
    assert category.average_price() == 150.0


# 3. Тесты абстрактного класса
def test_base_product_is_abstract():
    """Проверяем, что BaseProduct - абстрактный класс."""
    from abc import ABC
    assert issubclass(BaseProduct, ABC)


def test_cannot_instantiate_base_product():
    """Проверяем, что нельзя создать экземпляр абстрактного класса."""
    with pytest.raises(TypeError):
        BaseProduct("Test", "Desc", 100.0, 5)


# 4. Тесты инициализации
def test_product_init(sample_product):
    assert sample_product.name == "iPhone 15"
    assert sample_product.description == "Latest model"
    assert sample_product.price == 120000.0
    assert sample_product.quantity == 3


def test_smartphone_init(sample_smartphone):
    assert sample_smartphone.name == "Samsung S24"
    assert sample_smartphone.efficiency == 9.5
    assert sample_smartphone.model == "S24"
    assert sample_smartphone.memory == 256
    assert sample_smartphone.color == "Black"


def test_lawn_grass_init(sample_lawn_grass):
    assert sample_lawn_grass.name == "Green Grass"
    assert sample_lawn_grass.country == "Россия"
    assert sample_lawn_grass.germination_period == 14
    assert sample_lawn_grass.color == "Зеленый"


# 5. Наследование
def test_product_inherits_base_product():
    assert issubclass(Product, BaseProduct)


def test_smartphone_inherits_product():
    assert issubclass(Smartphone, Product)


def test_lawn_grass_inherits_product():
    assert issubclass(LawnGrass, Product)


# 6. Тесты миксина
def test_mixin_logger_is_parent():
    assert issubclass(Product, MixinLogger)


def test_mixin_logger_output(capsys):
    Product("Test Product", "Description", 100.0, 10)
    captured = capsys.readouterr()
    assert "Создан объект класса Product" in captured.out


def test_mixin_logger_smartphone_output(capsys):
    Smartphone("Test Phone", "Desc", 1000.0, 2, 9.0, "Model", 128, "Black")
    captured = capsys.readouterr()
    assert "Создан объект класса Smartphone" in captured.out


def test_mixin_logger_lawn_grass_output(capsys):
    LawnGrass("Test Grass", "Desc", 100.0, 10, "RU", 7, "Green")
    captured = capsys.readouterr()
    assert "Создан объект класса LawnGrass" in captured.out


# 7. Тесты Category
def test_category_init(sample_category):
    assert sample_category.name == "Mixed Category"
    assert len(sample_category.get_products_list()) == 3


def test_product_count_auto():
    initial_count = Category.product_count
    p1 = Product("P1", "D1", 100.0, 2)
    p2 = Smartphone("Phone", "Desc", 50000.0, 1, 8.0, "M1", 128, "Blue")
    Category("Test", "Desc", [p1, p2])
    assert Category.product_count == initial_count + 2


def test_category_count_auto():
    initial_count = Category.category_count
    Category("C1", "D1")
    Category("C2", "D2")
    assert Category.category_count == initial_count + 2


def test_add_product_valid(sample_category, sample_smartphone):
    initial_len = len(sample_category.get_products_list())
    sample_category.add_product(sample_smartphone)
    assert len(sample_category.get_products_list()) == initial_len + 1


def test_add_product_invalid_type():
    category = Category("Test", "Desc")
    with pytest.raises(TypeError):
        category.add_product("not a product")


# 8. Тесты цены
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


# 9. Тесты __str__
def test_product_str(sample_product):
    assert str(sample_product) == "iPhone 15, 120000.0 руб. Остаток: 3 шт."


def test_category_str(sample_products_list):
    category = Category("Test", "Desc", sample_products_list)
    assert str(category) == "Test, количество продуктов: 55 шт."


# 10. Тесты __add__
def test_product_add_same_type():
    p1 = Product("P1", "D1", 100.0, 5)
    p2 = Product("P2", "D2", 200.0, 3)
    assert p1 + p2 == 1100.0


def test_add_different_types_raises_error():
    phone = Smartphone("Phone", "D", 1000.0, 1, 9.0, "M", 128, "Black")
    grass = LawnGrass("Grass", "D", 100.0, 1, "RU", 7, "Green")
    with pytest.raises(TypeError):
        _ = phone + grass


# 11. Приватный атрибут
def test_products_is_private(sample_category):
    with pytest.raises(AttributeError):
        _ = sample_category.__products


# 12. Тест new_product
def test_new_product_classmethod():
    data = {"name": "Test", "description": "Desc", "price": 1000.0, "quantity": 5}
    product = Product.new_product(data)
    assert product.name == "Test"
    assert product.price == 1000.0
