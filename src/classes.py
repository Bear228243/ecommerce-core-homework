from typing import List, Optional


class Product:
    """Класс для представления товара."""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для категорий товаров."""
    name: str
    description: str
    products: List[Product]

    # Атрибуты класса (счетчики)
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        # Увеличиваем счетчики класса при создании объекта
        Category.category_count += 1
        Category.product_count += len(self.products)
