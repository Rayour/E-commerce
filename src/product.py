from typing import Any


class Product:
    """Класс для описания продукта"""

    name: str
    description: str
    price: float
    quantity: int

    products_lane: dict = {}

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Функция для создания объекта продукта
        с указанием названия, описания, цены и количества в наличии"""

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

        Product.products_lane[name] = self

    @classmethod
    def new_product(cls, name: str, description: str, price: float, quantity: int) -> Any:
        """Класс-метод для создания нового продукта с проверкой существования аналогичного продукта"""

        if name in Product.products_lane:
            Product.products_lane[name].price = max(Product.products_lane[name].price, price)
            Product.products_lane[name].quantity += quantity
            return Product.products_lane[name]
        else:
            return cls(name, description, price, quantity)
