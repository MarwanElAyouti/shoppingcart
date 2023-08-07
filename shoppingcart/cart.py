import typing

from . import abc
from .product_prices import DefaultProductPrices
from .currency import Currency 
from collections import OrderedDict

class ShoppingCart(abc.ShoppingCart):
    def __init__(self, product_prices: abc.ProductPriceDataSource = DefaultProductPrices(), currency_code: str = "EUR"):
        self._items = OrderedDict()
        self._product_prices = product_prices
        self._total_price = 0.0
        self._currency: Currency = Currency.get_currency(currency_code)

    def add_item(self, product_code: str, quantity: int):
        if product_code not in self._items:
            self._items[product_code] = quantity
        else:
            q = self._items[product_code]
            self._items[product_code] = q + quantity

        # Update the total price incrementally
        price = self._get_product_price(product_code) * quantity
        self._total_price += price


    def print_receipt(self) -> typing.List[str]:
        lines = []

        for product_code, quantity in self._items.items():
            price = self._get_product_price(product_code) * quantity

            price_string = self._format_price(price)

            lines.append(f"{product_code} - {quantity} - {price_string}")
        total_price_string = self._format_price(self._total_price)
        lines.append(f"Total - {total_price_string}")
        return lines
    
    def _get_product_price(self, product_code: str) -> float:
        return self._product_prices.get_product_price(product_code)
    
    def _format_price(self, amount: float) -> str:
        converted_price = self._currency.convert_from_euro(amount)
        return self._currency.format(converted_price)