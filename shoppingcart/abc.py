import abc
import typing
from decimal import Decimal

class ShoppingCart(abc.ABC):

    @abc.abstractmethod
    def add_item(self, product_code: str, quantity: int):
        pass

    @abc.abstractmethod
    def print_receipt(self) -> typing.List[str]:
        pass



class ProductPriceDataSource(abc.ABC):
    @abc.abstractmethod
    def get_product_price(self, product_code: str) -> Decimal:
        pass
