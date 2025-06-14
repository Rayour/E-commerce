import json
import os
from pathlib import Path

from src.category import Category
from src.product import Product

ROOT_PATH = Path(__file__).resolve().parents[1]


def read_json(file_path: str) -> list:
    """Функция получает путь до json файла,
    возвращает список словарей с данными о категориях и продуктах"""

    full_path = os.path.join(ROOT_PATH, file_path)
    data = []

    try:
        with open(full_path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except Exception as ex:
        print(f"En error occurred: {ex}")
    finally:
        return data


def create_categories(categories_list: list[dict]) -> list[Category]:
    """Функция получает на вход список словарей с данными о категориях товаров и товарами в них,
    возвращает список объектов категорий с вложенными объектами товаров"""

    categories = []

    for category in categories_list:
        products = []
        for product in category["products"]:
            products.append(Product(**product))
        category["products"] = products
        categories.append(Category(**category))

    return categories
