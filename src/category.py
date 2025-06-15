class Category:
    """Класс для описания категории продуктов"""

    name: str
    description: str
    products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list | None = None) -> None:
        """Функция для создания категории товаров
        с указанием названия, описания и входящих в данную категорию товаров"""

        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0
