from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any


class MixinLogger:
    """Миксин для логирования создания объектов."""

    def __init__(self, *args, **kwargs):
        print(f"Создан объект класса {self.__class__.__name__} с параметрами:")
        print(f"  {repr(self)}")
        super().__init__(*args, **kwargs)

    def __repr__(self):
        """Магический метод для представления объекта."""
        attrs = []
        for key, value in self.__dict__.items():
            if key.startswith('_') and not key.startswith('__'):
                continue
            attrs.append(f"{key}={value}")
        return f"{self.__class__.__name__}({', '.join(attrs)})"


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
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

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод строкового представления."""
        pass

    @abstractmethod
    def __add__(self, other: "BaseProduct") -> float:
        """Абстрактный метод сложения продуктов."""
        pass


class Product(MixinLogger, BaseProduct):
    """Класс для представления товара."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__(name=name, description=description, price=price, quantity=quantity)

    @classmethod
    def new_product(cls, product_data: Dict[str, Any]) -> "Product":
        """Класс-метод для создания продукта из словаря."""
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"]
        )

    def __str__(self) -> str:
        """Строковое представление продукта."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Сложение продуктов: цена * количество."""
        if not isinstance(other, type(self)):
            raise TypeError("Нельзя складывать товары разных классов")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    """Класс-наследник для смартфонов."""
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс-наследник для травы газонной."""
    country: str
    germination_period: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    """Класс для категорий товаров."""
    name: str
    description: str
    __products: List[Product]

    # Атрибуты класса (счетчики)
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в приватный список с проверкой типа."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product или его наследников")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для вывода списка продуктов."""
        if not self.__products:
            return "В категории нет товаров."

        result = ""
        for product in self.__products:
            result += str(product) + "\n"
        return result.strip()

    def __str__(self) -> str:
        """Строковое представление категории."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def get_products_list(self) -> List[Product]:
        """Вспомогательный метод для тестов."""
        return self.__products

    def average_price(self) -> float:
        """Метод подсчета среднего ценника всех товаров в категории."""
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0.0
