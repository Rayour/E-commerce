from src.product import Product


class Order:
    """Класс для описания заказа"""
    product: Product
    amount: int
    __total: float

    def __init__(self, product: Product, amount: int) -> None:
        """Метод инициализации заказа"""
        self.product = product
        self.amount = amount
        self.__total = product.price * amount

    @property
    def total(self) -> float:
        return self.__total
