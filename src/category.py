from src.product import Product


class Category:
    """Класс для описания категории продуктов"""

    name: str
    description: str
    __products: list

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list | None = None) -> None:
        """Функция для создания категории товаров
        с указанием названия, описания и входящих в данную категорию товаров"""

        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self) -> str:
        products_count = 0
        for product in self.__products:
            products_count += product.quantity
        return f"{self.name}, количество продуктов: {products_count} шт."

    @property
    def products(self) -> str:
        products_list = ""
        for product in self.__products:
            products_list += f"{str(product)}\n"
        return products_list

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию"""

        self.__products.append(product)
        Category.product_count += 1
