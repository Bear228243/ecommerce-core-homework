from src.classes import Product, Category

if __name__ == "__main__":
    # Создаем продукты через класс-метод
    product1_data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }
    product2_data = {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
    }
    product3_data = {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
    }

    product1 = Product.new_product(product1_data)
    product2 = Product.new_product(product2_data)
    product3 = Product.new_product(product3_data)

    print("=== ТОВАРЫ ===")
    print(f"1. {product1.name} - {product1.price} руб. (в наличии: {product1.quantity} шт.)")
    print(f"2. {product2.name} - {product2.price} руб. (в наличии: {product2.quantity} шт.)")
    print(f"3. {product3.name} - {product3.price} руб. (в наличии: {product3.quantity} шт.)")

    # Создаем категорию
    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций",
                         [product1, product2, product3])

    print("\n=== КАТЕГОРИЯ ===")
    print(f"Название: {category1.name}")
    print("Товары в категории:")
    print(category1.products)  # Используем геттер

    print("\n=== СЧЕТЧИКИ ===")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")

    # Добавляем новый продукт через add_product
    print("\n=== ДОБАВЛЯЕМ НОВЫЙ ПРОДУКТ ===")
    product4 = Product("Nothing Phone 2", "256GB, White", 65000.0, 6)
    category1.add_product(product4)

    print("Обновленный список товаров:")
    print(category1.products)
    print(f"Всего товаров теперь: {Category.product_count}")

    # Тестируем сеттер цены
    print("\n=== ТЕСТ СЕТТЕРА ЦЕНЫ ===")
    print(f"Старая цена iPhone: {product2.price}")
    product2.price = 200000.0
    print(f"Новая цена iPhone: {product2.price}")
    print("Попытка установить отрицательную цену:")
    product2.price = -1000  # Должно вывести сообщение об ошибке
    print(f"Цена после попытки установить -1000: {product2.price}")
