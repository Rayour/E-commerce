import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_category_init(first_category: Category, second_category: Category, third_category: Category,
                       second_product: Product) -> None:
    assert first_category.name == "Техника"
    assert first_category.description == "Бытовая техника различного назначения"
    assert first_category.products == """Холодильник, 90000.0 руб. Остаток: 5 шт.
Микроволновка, 3000.0 руб. Остаток: 7 шт.\n"""

    assert second_category.name == "Продукты"
    assert second_category.description == "Всё, что можно съесть"
    assert second_category.products == """Шоколадка, 200.0 руб. Остаток: 55 шт.
Чипсы, 170.0 руб. Остаток: 77 шт.\n"""

    assert third_category.name == "Отдых"
    assert third_category.description == "Всё для отдыха"

    assert first_category.category_count == 3
    assert second_category.product_count == 4

    third_category.add_product(second_product)
    assert third_category.product_count == 5


def test_category_str(first_category: Category) -> None:
    assert str(first_category) == "Техника, количество продуктов: 12 шт."


def test_add_product(
        first_category: Category, product: Product, smartphone: Smartphone, lawn_grass: LawnGrass) -> None:
    assert len(first_category._products) == 2
    first_category.add_product(product)
    assert len(first_category._products) == 3
    first_category.add_product(smartphone)
    assert len(first_category._products) == 4
    first_category.add_product(lawn_grass)
    assert len(first_category._products) == 5

    with pytest.raises(TypeError):
        first_category.add_product(3)  # type: ignore[arg-type]


def test_middle_price(first_category: Category, third_category: Category) -> None:
    assert first_category.middle_price() == 46500.0
    assert third_category.middle_price() == 0.0
