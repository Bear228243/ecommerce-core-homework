from src.classes import Product, Category

if __name__ == "__main__":
    # Создаем товары
    iphone = Product("iPhone 15", "Смартфон от Apple", 120000.0, 5)
    samsung = Product("Samsung S24", "Флагманский смартфон", 90000.0, 3)

    # Создаем категорию
    smartphones = Category("Смартфоны", "Мобильные телефоны", [iphone, samsung])

    # Проверяем счетчики
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")

    # Проверяем содержимое
    print(f"Товары в категории '{smartphones.name}':")
    for product in smartphones.products:
        print(f"  - {product.name}: {product.price} руб.")
