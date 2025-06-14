

class Product:
    """Класс для описания продукта"""

    name: str
    description: str
    price: float
    quantity: int


    def __init__(self, name, description, price, quantity):
        """Функция для создания объекта продукта
        с указанием названия, описания, цены и количества в наличии"""

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
