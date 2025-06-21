import pytest

from src.category import Category
from src.product_iterator import ProductIterator


def test_product_iterator(first_category: Category) -> None:
    iterator = ProductIterator(first_category)
    assert next(iterator).name == "Холодильник"
    assert next(iterator).name == "Микроволновка"

    with pytest.raises(StopIteration):
        next(iterator)
