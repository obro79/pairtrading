"""Porfolio class that stores current portfolio value and current holdings."""
from data import Data


class Portfolio:
    def __init__(self, initial_balance, asset_a, asset_b, date_range):
        self.total_value = initial_balance
        self.current_cash = initial_balance
        self.data = Data(asset_a, asset_b, date_range)
        self.current_holdings = {}

        @property
        def total_value(self):
            return self.current_cash + get_current_holdings_value(self)

        @property
        def current_cash(self):
            return self.current_cash

        @current_cash.setter
        def current_cash(self, cash):
            self.current_cash = cash

        @property
        def current_holdings(self):
            return self.current_holdings

        @current_holdings.setter
        def current_holdings(self, holdings):
            for holding in holdings:
                self.current_holdings[holding] = holdings[holding]

        def get_current_holdings_value(self):
            """
            Summary: Returns the value of the current holdings.
            Args: self
            Returns: current_holdings_value: float
            """
            if self.current_holdings == []:
                return 0
            else:
                current_holdings_value = 0
                for holding in self.current_holdings:
                    current_holdings_value += get_holding_value(holding)
                return current_holdings_value

        def get_holding_value(self, asset):
            """
            Summary: Returns the value of the current holding.
            Args: self, asset: str
            Returns: holding_value: float
            """
            return self.data.get_price_on_data(asset, self.data.date_range) * self.current_holdings[asset]
