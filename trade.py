class Trade:
    def __init__(self, date, asset, price, quantity, commission):
        self.date = date
        self.asset = asset
        self.price = price
        self.quantity = quantity
        self.commission = commission

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        self._date = value

    @property
    def asset(self):
        return self._asset

    @asset.setter
    def asset(self, value):
        self._asset = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @property
    def commission(self):
        return self.commission

    def make_trade(self):
        pass