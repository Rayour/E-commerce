from typing import Any

import pytest

from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_product_init(product: Product) -> None:
    assert product.name == "Шоколадка"
    assert product.description == "Вкусно и калорийно"
    assert product.price == 200.0
    assert product.quantity == 55


def test_product_init_raise() -> None:
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Name", "Description", 100.0, 0)


def test_create_new_product() -> None:
    p1 = Product.new_product("Булочка", "Вкусно и калорийно", 200.0, 55)
    assert p1.name == "Булочка"
    assert p1.price == 200.0
    assert p1.quantity == 55
    p2 = Product.new_product("Булочка", "Вкусно и калорийно", 250.0, 45)
    assert p1.price == 250.0
    assert p1.quantity == 100
    assert p1 == p2


def test_product_str(product: Product) -> None:
    assert str(product) == "Шоколадка, 200.0 руб. Остаток: 55 шт."


def test_price_change(capsys: Any, product: Product) -> None:
    product.price = 500.0
    assert product.price == 500.0
    product.price = -200.0
    assert capsys.readouterr().out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"


def test_product_add(product: Product, second_product: Product, smartphone: Smartphone, smartphone2: Smartphone,
                     lawn_grass: LawnGrass, lawn_grass2: LawnGrass) -> None:
    assert product + second_product == 147000.0
    assert smartphone + smartphone2 == 2114000.0
    assert lawn_grass + lawn_grass2 == 16750.0
    assert product + smartphone == 445000.0
    with pytest.raises(TypeError):
        product + 3
    with pytest.raises(TypeError):
        smartphone + lawn_grass
