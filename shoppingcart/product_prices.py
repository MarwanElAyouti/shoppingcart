import json
import csv
from . import abc
from decimal import Decimal


class DefaultProductPrices(abc.ProductPriceDataSource):
    def __init__(self) -> None:
        self._prices = {
            "apple": 1.0,
            "banana" : 1.1,
            "kiwi" : 3.0
        }
    
    def get_product_price(self, product_code: str) -> Decimal:
        return self._prices.get(product_code, 0.0)


class JSONProductPrices(abc.ProductPriceDataSource):
    def __init__(self, filename: str):
        with open(filename, 'r') as file:
            self._prices = json.load(file)

    def get_product_price(self, product_code: str) -> Decimal:
        return Decimal(self._prices.get(product_code, 0.0))


class CSVProductPrices(abc.ProductPriceDataSource):
    def __init__(self, filename: str):
        self._prices = {}
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self._prices[row['product_code']] = Decimal(row['price'])


    def get_product_price(self, product_code: str) -> Decimal:
        return Decimal(self._prices.get(product_code, 0.0))