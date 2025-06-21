from src.category import Category
from src.product import Product


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
