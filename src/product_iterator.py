from typing import Any, Iterator

from src.category import Category


class ProductIterator:
    """Класс-итератор для итерации продуктов в категории"""

    category: Category
    index: int

    def __init__(self, category: Category):
        """Метод инициализации итератора продуктов категории"""

        self.category = category
        self.index = 0

    def __iter__(self) -> Iterator:
        """Метод создания итератора"""
        self.index = 0
        return self

    def __next__(self) -> Any:
        if self.index < len(self.category._products):
            product = self.category._products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration
