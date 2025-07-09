"""Trade class that stores trade information."""
import CONSTANTS


class Trade:
    def __init__(self, date, asset: str, price: float, quantity: float, commission=CONSTANTS.COMMISSION) -> None:
        self.date = date
        self.asset = asset
        self.price = price
        self.quantity = quantity
        self.commission = commission

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value) -> None:
        self._date = value

    @property
    def asset(self) -> str:
        return self._asset

    @asset.setter
    def asset(self, value) -> None:
        self._asset = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value) -> None:
        self._price = value

    @property
    def quantity(self) -> float:
        return self._quantity

    @quantity.setter
    def quantity(self, value) -> None:
        self._quantity = value

    @property
    def commission(self) -> float:
        return self.commission

    def make_trade(self, action, ):
        pass
