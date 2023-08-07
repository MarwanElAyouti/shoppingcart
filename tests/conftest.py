import pytest
import csv
import json
from shoppingcart.cart import ShoppingCart
from shoppingcart.product_prices import CSVProductPrices, JSONProductPrices

@pytest.fixture
def cart() -> ShoppingCart:
  return ShoppingCart()

@pytest.fixture
def product_prices_json(tmp_path):
    product_prices = {
        "apple": 1.0,
        "banana": 1.1,
        "kiwi": 3.0,
        "orange": 0.5
    }

    # Create a temporary JSON file for testing
    file_path = tmp_path / "test_product_prices.json"
    with open(file_path, "w") as f:
        json.dump(product_prices, f)

    return file_path

@pytest.fixture
def product_prices_csv(tmp_path):
    product_prices = [
        {"product_code": "apple", "price": "1.0"},
        {"product_code": "banana", "price": "1.1"},
        {"product_code": "kiwi", "price": "3.0"},
        {"product_code": "mango", "price": "1.5"}
    ]

    # Create a temporary CSV file for testing
    file_path = tmp_path / "test_product_prices.csv"
    with open(file_path, "w", newline="") as f:
        fieldnames = ["product_code", "price"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(product_prices)

    return file_path


@pytest.fixture
def cart_json(product_prices_json):
    product_prices_json = JSONProductPrices(product_prices_json)
    return ShoppingCart(product_prices_json)


@pytest.fixture
def cart_csv(product_prices_csv):
    product_prices_csv = CSVProductPrices(product_prices_csv)
    return ShoppingCart(product_prices_csv)