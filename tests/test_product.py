from src.product import Product


def test_product_init(product: Product) -> None:
    assert product.name == "Шоколадка"
    assert product.description == "Вкусно и калорийно"
    assert product.price == 200.0
    assert product.quantity == 55
