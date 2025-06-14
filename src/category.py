

class Category:
    """Класс для описания категории продуктов"""

    name: str
    description: str
    products: list

    categories_count = 0
    products_count = 0


    def __init__(self, name, description, products=None):
        """Функция для создания категории товаров
        с указанием названия, описания и входящих в данную категорию товаров"""

        self.name = name
        self.description = description
        self.products = products if products else []
        self.categories_count += 1
        self.products_count += len(products) if products else 0
