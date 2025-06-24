from typing import Any

from src.product import Product


class Category:
    """Класс для описания категории продуктов"""

    name: str
    description: str
    _products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list | None = None) -> None:
        """Функция для создания категории товаров
        с указанием названия, описания и входящих в данную категорию товаров"""

        self.name = name
        self.description = description
        self._products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self) -> str:
        """Метод строкового представления объекта категории.
        В качестве количества продуктов возвращается суммарное количество всех продуктов данной категории"""

        products_count = 0
        for product in self._products:
            products_count += product.quantity
        return f"{self.name}, количество продуктов: {products_count} шт."

    @property
    def products(self) -> str:
        products_list = ""
        for product in self._products:
            products_list += f"{str(product)}\n"
        return products_list

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию"""

        if isinstance(product, Product):
            self._products.append(product)
            Category.product_count += 1
        else:
            raise TypeError(
                "В список товаров категории можно добавить только объект класса Product или его наследников"
            )

    def middle_price(self) -> Any:
        """Метод для подсчета средней цены товара в категории"""

        try:
            return round(sum([item.price for item in self._products]) / len(self._products), 2)
        except ZeroDivisionError:
            return 0.0
