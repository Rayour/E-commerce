from src.product import Product


def test_product_init(product: Product) -> None:
    assert product.name == "Шоколадка"
    assert product.description == "Вкусно и калорийно"
    assert product.price == 200.0
    assert product.quantity == 55


def test_create_new_product() -> None:
    p1 = Product.new_product("Булочка", "Вкусно и калорийно", 200.0, 55)
    assert p1.name == "Булочка"
    assert p1.price == 200.0
    assert p1.quantity == 55
    p2 = Product.new_product("Булочка", "Вкусно и калорийно", 250.0, 45)
    assert p1.price == 250.0
    assert p1.quantity == 100
    assert p1 == p2
