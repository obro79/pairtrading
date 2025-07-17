"""Backtest class that runs the trading strategy on historical data."""
from datetime import *

import pandas as pd

import CONSTANTS
from date_range import DateRange
from portfolio import Portfolio
from strategy import Strategy


class Backtest:
    def __init__(self, asset_a_data: pd.DataFrame, asset_b_data: pd.DataFrame, transaction_cost=CONSTANTS.COMMISSION,
                 start_date='2020-01-01',
                 end_date=datetime.now()) -> None:

        self._transaction_cost = transaction_cost
        self._asset_a_data = asset_a_data
        self._asset_b_data = asset_b_data
        self._date_range = DateRange(start_date, end_date)
        self._portfolio = Portfolio(initial_balance=CONSTANTS.STARTING_VALUE, date_range=self.date_range)  ##
        self._strategy = Strategy(asset_a=self.asset_a_data,
                                  asset_b=self.asset_b_data)  ##TODO need access to ticker not data

        self._nav_history: Dict[datetime, float] = {}
        self.backtest()

    @property
    def transaction_cost(self) -> float:
        return self._transaction_cost

    @property
    def asset_a_data(self) -> pd.DataFrame:
        return self._asset_a_data

    @property
    def asset_b_data(self) -> pd.DataFrame:
        return self._asset_b_data

    def backtest(self):
        for date in self.date_range:
            next_action = self.strategy.get_next_action(date)
            if next_action == 0:
                continue
            elif next_action == 1:
                makeTrade()

    def backtest_metrics(self):
        return {
            "max_drawdown": self.max_drawdown(),
            "annual_return": self.annual_return(),
            "annual_volatility": self.annual_volatility(),
            "calmar_ratio": self.calmar_ratio(),
            "sharpe_ratio": self.sharpe_ratio(),
            "sortino_ratio": self.sortino_ratio(),
            "alpha": self.alpha(),
            "beta": self.beta()
        }

    def plot_results(self):
        pass

    def sortino_ratio(self):
        pass

    def sharpe_ratio(self):
        pass

    def max_drawdown(self):
        pass

    def annual_return(self):
        pass

    def annual_volatility(self):
        pass

    def calmar_ratio(self):
        pass

    def alpha(self):
        pass

    def beta(self):
        pass
