from src.classes import Product, Category, Smartphone, LawnGrass

if __name__ == "__main__":
    print("=== СОЗДАЕМ ТОВАРЫ ===")

    # Обычный продукт
    charger = Product("Зарядное устройство", "Быстрая зарядка 65W", 2500.0, 15)
    print(charger)

    # Смартфон
    smartphone = Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
        efficiency=9.8,
        model="S23 Ultra",
        memory=256,
        color="Серый"
    )
    print(smartphone)

    # Трава газонная
    grass = LawnGrass(
        name="Газонная трава Премиум",
        description="Быстрорастущая, морозостойкая",
        price=750.0,
        quantity=200,
        country="Россия",
        germination_period=10,
        color="Изумрудный"
    )
    print(grass)

    print("\n=== СОЗДАЕМ КАТЕГОРИИ ===")

    electronics = Category("Электроника", "Техника и аксессуары", [charger, smartphone])
    print(electronics)
    print("Товары в категории:")
    print(electronics.products)

    garden = Category("Сад и огород", "Все для сада", [grass])
    print(garden)
    print(garden.products)

    print("\n=== ПРОВЕРКА СЛОЖЕНИЯ ===")

    smartphone2 = Smartphone(
        name="iPhone 15",
        description="512GB, Titanium",
        price=210000.0,
        quantity=3,
        efficiency=9.7,
        model="15 Pro",
        memory=512,
        color="Titanium"
    )

    # Сложение двух смартфонов (работает)
    print(f"Сумма двух смартфонов: {smartphone + smartphone2} руб.")

    # Попытка сложить смартфон и траву (ошибка)
    print("\nПопытка сложить смартфон и траву:")
    try:
        result = smartphone + grass
        print(f"Результат: {result}")
    except TypeError as e:
        print(f"Ошибка: {e}")

    print("\n=== ДОБАВЛЕНИЕ ТОВАРОВ ===")

    new_phone = Smartphone(
        name="Xiaomi 14",
        description="512GB, White",
        price=85000.0,
        quantity=7,
        efficiency=9.2,
        model="14",
        memory=512,
        color="White"
    )

    electronics.add_product(new_phone)
    print(f"После добавления: {electronics}")
    print(electronics.products)

    # Попытка добавить не-товар (ошибка)
    print("\nПопытка добавить строку вместо товара:")
    try:
        electronics.add_product("Это не товар")
    except TypeError as e:
        print(f"Ошибка: {e}")

    print("\n=== ИТОГОВЫЕ СЧЕТЧИКИ ===")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")
