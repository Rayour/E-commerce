import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def first_category() -> Category:
    return Category(
        name="Техника",
        description="Бытовая техника различного назначения",
        products=[
            Product("Холодильник", "Отлично охлаждает", 90000.0, 5),
            Product("Микроволновка", "Отлично нагревает", 3000.0, 7),
        ]
    )


@pytest.fixture
def second_category() -> Category:
    return Category(
        name="Продукты",
        description="Всё, что можно съесть",
        products=[
            Product("Шоколадка", "Вкусно и калорийно", 200.0, 55),
            Product("Чипсы", "Вкусно и вредно", 170.0, 77),
        ]
    )


@pytest.fixture
def third_category() -> Category:
    return Category(
        name="Отдых",
        description="Всё для отдыха"
    )


@pytest.fixture
def product() -> Product:
    return Product("Шоколадка", "Вкусно и калорийно", 200.0, 55)
