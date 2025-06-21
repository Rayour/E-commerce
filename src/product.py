from typing import Any


class Product:
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

        Product.products_lane[name] = self

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
    def new_product(cls, name: str, description: str, price: float, quantity: int) -> Any:
        """Класс-метод для создания нового продукта с проверкой существования аналогичного продукта"""

        if name in Product.products_lane:
            Product.products_lane[name].__price = max(Product.products_lane[name].__price, price)
            Product.products_lane[name].quantity += quantity
            return Product.products_lane[name]
        else:
            return cls(name, description, price, quantity)

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
