class PrintMixin:
    """Класс миксин для вывода информации о продукте при его инициализации"""

    def __init__(self) -> None:
        print(repr(self))
