from src.classes import Product, Category

if __name__ == "__main__":
    print("=== ТЕСТ ИСКЛЮЧЕНИЙ ===\n")

    # Попытка создать товар с нулевым количеством
    print("Попытка создать товар с quantity=0:")
    try:
        bad_product = Product("Плохой товар", "Не должен создаться", 100.0, 0)
    except ValueError as e:
        print(f"Ошибка: {e}")

    print("\nПопытка создать товар с quantity=5:")
    good_product = Product("Хороший товар", "Создается нормально", 200.0, 5)
    print(f"Создан: {good_product}")

    print("\n=== СРЕДНИЙ ЦЕННИК ===\n")

    # Создаем категорию с товарами
    p1 = Product("Товар 1", "Описание 1", 100.0, 10)
    p2 = Product("Товар 2", "Описание 2", 300.0, 5)
    p3 = Product("Товар 3", "Описание 3", 500.0, 2)

    category = Category("Тестовая категория", "Для проверки", [p1, p2, p3])

    print(f"Категория: {category}")
    print(f"Средний ценник: {category.average_price()} руб.")
    # Ожидается: (100 + 300 + 500) / 3 = 300.0

    print("\nПроверка пустой категории:")
    empty_category = Category("Пустая", "Нет товаров")
    print(f"Средний ценник пустой категории: {empty_category.average_price()} руб.")

    print("\n=== ДОБАВЛЕНИЕ ТОВАРА ===")
    p4 = Product("Товар 4", "Описание 4", 700.0, 3)
    category.add_product(p4)
    print("После добавления товара за 700 руб.:")
    print(f"Средний ценник: {category.average_price()} руб.")
    # Ожидается: (100 + 300 + 500 + 700) / 4 = 400.0
