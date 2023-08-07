from enum import Enum


class CurrencySymbol(Enum):
    USD = "$"
    EUR = "€"
    GBP = "£"
    JPY = "¥"
    # Add more currency codes and symbols as needed

class Currency:
    def __init__(self, code: str = "EUR", symbol: str = CurrencySymbol.EUR.value, conversion_rate_from_eur: float = 1.0):
        self.code = code
        self.symbol = symbol
        self.conversion_rate_from_eur = conversion_rate_from_eur

    def format(self, amount: float) -> str:
        return f"{self.symbol}{amount:.2f}"

    def convert_from_euro(self, amount: float) -> float:
        if self.code == "EUR":
            return amount
        return amount * self.conversion_rate_from_eur 
    

    @classmethod
    def get_currency(cls, code: str) -> 'Currency':
        currencies = {
            "USD": Currency("USD", CurrencySymbol.USD.value, 1.12),
            "EUR": Currency("EUR", CurrencySymbol.EUR.value, 1.0),
            "GBP": Currency("GBP", CurrencySymbol.GBP.value, 0.86),
            "JPY": Currency("JPY", CurrencySymbol.JPY.value, 129.53),
            # Add more currencies as needed
        }
        return currencies.get(code)
