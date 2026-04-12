from typing import List, Optional, Dict, Any


class Product:
    """Класс для представления товара."""
    name: str
    description: str
    __price: float  # Приватный атрибут
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для цены с проверкой."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data: Dict[str, Any]) -> "Product":
        """Класс-метод для создания продукта из словаря."""
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"]
        )

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"


class Category:
    """Класс для категорий товаров."""
    name: str
    description: str
    __products: List[Product]  # Приватный атрибут

    # Атрибуты класса (счетчики)
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        # Увеличиваем счетчики класса
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в приватный список."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для вывода списка продуктов в читаемом формате."""
        if not self.__products:
            return "В категории нет товаров."

        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result.strip()

    def get_products_list(self) -> List[Product]:
        """Вспомогательный метод для тестов (возвращает список продуктов)."""
        return self.__products

    def __repr__(self):
        return f"Category(name='{self.name}', products_count={len(self.__products)})"
