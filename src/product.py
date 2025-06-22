from typing import Any

from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """Класс для описания продукта"""

    name: str
    description: str
    __price: float
    quantity: int

    products_lane: dict = {}

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Функция для создания объекта продукта
        с указанием названия, описания, цены и количества в наличии"""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

        Product.products_lane[name] = self

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        """Метод строкового представления объекта продукта"""

        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> float:
        """Метод сложения продуктов. Возвращает суммарную стоимость всех единиц товаров в складываемых продуктах"""

        if isinstance(other, self.__class__):
            return self.quantity * self.__price + other.quantity * other.__price
        else:
            raise TypeError("Сложить можно только два объекта одного класса")

    @classmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> Any:
        """Класс-метод для создания нового продукта с проверкой существования аналогичного продукта"""

        if args[0] in cls.products_lane:
            cls.products_lane[args[0]].__price = max(cls.products_lane[args[0]].__price, args[2])
            cls.products_lane[args[0]].quantity += args[3]
            return cls.products_lane[args[0]]
        else:
            return cls(*args)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float) -> None:
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif 0 < price < self.__price:
            accept = input("Указанная цена ниже текущей. Изменить цену? (Y)es/N(o)").lower()
            if accept == "y":
                self.__price = price
        else:
            self.__price = price
