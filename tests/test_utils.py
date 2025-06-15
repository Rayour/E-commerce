from typing import Any

import pytest

import src.utils


@pytest.mark.parametrize("data_to_create_categories_with_products", [i for i in range(2)], indirect=True)
def test_create_categories(data_to_create_categories_with_products: Any) -> None:
    result = src.utils.create_categories(data_to_create_categories_with_products["input"])
    assert result[0].name == data_to_create_categories_with_products["output"]["name"]
    assert result[0].description == data_to_create_categories_with_products["output"]["description"]
    assert result[0].product_count == data_to_create_categories_with_products["output"]["product_count"]
