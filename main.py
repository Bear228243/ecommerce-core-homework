from src.classes import Product, Category

if __name__ == "__main__":
    # Создаем продукты
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print("=== ТОВАРЫ ===")
    print(str(product1))
    print(str(product2))
    print(str(product3))

    # Создаем категорию
    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации",
                         [product1, product2, product3])

    print("\n=== КАТЕГОРИЯ ===")
    print(str(category1))
    print("\nТовары в категории:")
    print(category1.products)

    print("\n=== СЛОЖЕНИЕ ТОВАРОВ ===")
    print(f"Сумма product1 + product2: {product1 + product2} руб.")

    # Добавляем новый продукт
    print("\n=== ДОБАВЛЯЕМ ПРОДУКТ ===")
    product4 = Product("Nothing Phone 2", "256GB, White", 65000.0, 6)
    category1.add_product(product4)
    print(str(category1))
    print(category1.products)

    print("\n=== СЧЕТЧИКИ ===")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")