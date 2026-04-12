from src.classes import Product, Category

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print("=== ТОВАРЫ ===")
    print(f"1. {product1.name} - {product1.price} руб. (в наличии: {product1.quantity} шт.)")
    print(f"2. {product2.name} - {product2.price} руб. (в наличии: {product2.quantity} шт.)")
    print(f"3. {product3.name} - {product3.price} руб. (в наличии: {product3.quantity} шт.)")

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print("\n=== КАТЕГОРИЯ 1 ===")
    print(f"Название: {category1.name}")
    print(f"Количество товаров в категории: {len(category1.products)}")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров во всех категориях: {Category.product_count}")

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print("\n=== КАТЕГОРИЯ 2 ===")
    print(f"Название: {category2.name}")
    print(f"Количество товаров в категории: {len(category2.products)}")

    print("\n=== ИТОГОВЫЕ СЧЕТЧИКИ ===")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")
