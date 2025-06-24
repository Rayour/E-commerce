from src.order import Order
from src.product import Product


def test_order_init(product: Product) -> None:
    order = Order(product, 10)
    assert order.amount == 10
    assert order.total == 2000.0
