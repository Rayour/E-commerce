from src.category import Category
from src.product import Product


def test_category_init(first_category: Category, second_category: Category, third_category: Category,
                       second_product: Product) -> None:
    assert first_category.name == "Техника"
    assert first_category.description == "Бытовая техника различного назначения"
    assert len(first_category.products) == 2

    assert second_category.name == "Продукты"
    assert second_category.description == "Всё, что можно съесть"
    assert len(second_category.products) == 2

    assert third_category.name == "Отдых"
    assert third_category.description == "Всё для отдыха"
    assert len(third_category.products) == 0

    assert first_category.category_count == 3
    assert second_category.product_count == 4

    third_category.add_product(second_product)
    assert len(third_category.products) == 1
    assert third_category.product_count == 5
