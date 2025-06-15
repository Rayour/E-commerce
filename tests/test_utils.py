from typing import Any

import pytest

import src.utils


@pytest.mark.parametrize("data_to_create_categories_with_products", [i for i in range(2)], indirect=True)
def test_create_categories(data_to_create_categories_with_products: Any) -> None:
    result = src.utils.create_categories(data_to_create_categories_with_products["input"])
    assert result[0].name == data_to_create_categories_with_products["output"]["name"]
    assert result[0].description == data_to_create_categories_with_products["output"]["description"]
    assert len(result[0].products) == data_to_create_categories_with_products["output"]["product_len"]
    if data_to_create_categories_with_products["output"]["product_len"] > 0:
        assert result[0].products[0].name == data_to_create_categories_with_products["output"]["product_0_name"]
        assert result[0].products[1].description == \
               data_to_create_categories_with_products["output"]["product_1_description"]
        assert result[0].products[2].price == data_to_create_categories_with_products["output"]["product_2_price"]
        assert result[0].products[2].quantity == \
               data_to_create_categories_with_products["output"]["product_2_quantity"]
