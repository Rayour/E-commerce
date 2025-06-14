from src.category import Category


def test_category_init(first_category: Category, second_category: Category, third_category: Category) -> None:
    assert first_category.name == "Техника"
    assert first_category.description == "Бытовая техника различного назначения"
    assert len(first_category.products) == 2

    assert second_category.name == "Продукты"
    assert second_category.description == "Всё, что можно съесть"
    assert len(second_category.products) == 2

    assert third_category.name == "Отдых"
    assert third_category.description == "Всё для отдыха"
    assert len(third_category.products) == 0

    assert first_category.categories_count == 3
    assert first_category.products_count == 4
