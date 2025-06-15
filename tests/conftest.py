from typing import Any

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


@pytest.fixture
def second_product() -> Product:
    return Product("Палатка", "Уютно и комфортно", 17000.0, 8)


@pytest.fixture
def data_to_create_categories_with_products(request: Any) -> Any:
    """Фикстура для тестирования функции src.utils.create_categories"""

    tests = [
        {
            "input": [
                {
                    "name": "Смартфоны",
                    "description": "Смартфоны, как средство коммуникации",
                    "products": [
                        {
                            "name": "Samsung Galaxy C23 Ultra",
                            "description": "256GB, Серый цвет, 200MP камера",
                            "price": 180000.0,
                            "quantity": 5
                        },
                        {
                            "name": "Iphone 15",
                            "description": "512GB, Gray space",
                            "price": 210000.0,
                            "quantity": 8
                        },
                        {
                            "name": "Xiaomi Redmi Note 11",
                            "description": "1024GB, Синий",
                            "price": 31000.0,
                            "quantity": 14
                        }
                    ]
                }
            ],
            "output": {
                "name": "Смартфоны",
                "description": "Смартфоны, как средство коммуникации",
                "product_len": 3,
                "product_0_name": "Samsung Galaxy C23 Ultra",
                "product_1_description": "512GB, Gray space",
                "product_2_price": 31000.0,
                "product_2_quantity": 14
            }
        },
        {
            "input": [
                {
                    "name": "Смартфоны",
                    "description": "Смартфоны, как средство коммуникации",
                    "products": []
                }
            ],
            "output": {
                "name": "Смартфоны",
                "description": "Смартфоны, как средство коммуникации",
                "product_len": 0,
                "product_0_name": "",
                "product_1_description": "",
                "product_2_price": 0,
                "product_2_quantity": 0
            }
        }
    ]
    return tests[request.param]
