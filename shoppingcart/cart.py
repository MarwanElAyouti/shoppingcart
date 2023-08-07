import typing

from . import product_prices
from . import abc
from collections import OrderedDict

class ShoppingCart(abc.ShoppingCart):
    def __init__(self, product_prices: abc.ProductPriceDataSource = product_prices.DefaultProductPrices()):
        self._items = OrderedDict()
        self._product_prices = product_prices
        self._total_price = 0.0

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

            price_string = "€%.2f" % price

            lines.append(f"{product_code} - {quantity} - {price_string}")

        lines.append(f"Total - €{self._total_price:.2f}")
        return lines

    def _get_product_price(self, product_code: str) -> float:
        return self._product_prices.get_product_price(product_code)
    