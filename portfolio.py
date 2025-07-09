"""Portfolio class that stores current portfolio value and current holdings."""
import pandas as pd

from data import Data
from date_range import DateRange
from trades import Trades


class Portfolio:
    def __init__(self, initial_balance: float, asset_a: pd.DataFrame, asset_b: pd.DataFrame,
                 date_range: DateRange) -> None:
        self.total_value = initial_balance
        self.current_cash = initial_balance
        self.data = Data(asset_a, asset_b, date_range)
        self.current_holdings = {}
        self.trades = Trades()

    @property
    def total_value(self) -> float:
        return self.current_cash + self.get_current_holdings_value()

    @property
    def current_cash(self) -> float:
        return self.current_cash

    @current_cash.setter
    def current_cash(self, cash: float) -> None:
        self.current_cash = cash

    @property
    def current_holdings(self) -> list[str]:
        return self.current_holdings

    @current_holdings.setter
    def current_holdings(self, holdings: list[str]) -> None:
        for holding in holdings:
            self.current_holdings[holding] = holdings[holding]

    def get_current_holdings_value(self) -> float:
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
                current_holdings_value += self.get_holding_value(holding)
            return current_holdings_value

    def get_holding_value(self, asset: str) -> float:
        """
        Summary: Returns the value of the current holding.
        Args: self, asset: str
        Returns: holding_value: float
        """
        return self.data.get_price_on_data(asset, self.data.date_range) * self.current_holdings[asset]

    def make_trade(self, asset_a: str, asset_b: str, action=0) -> None:
        if action == 1:
            pass

            self.trades.add_trade(action, asset_a, asset_b)

        elif action == -1:
            pass
