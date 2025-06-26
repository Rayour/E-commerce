from typing import Any


class ZeroQuantityException(Exception):
    """Класс для исключения при добавлении товара с 0 количеством"""

    def __init__(self, *args: Any, **kwargs: Any):
        """Метод инициализации исключения"""
        self.message = args[0] if args[0] else "Нельзя добавить товар с нулевым количеством"
