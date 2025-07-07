"""Backtest class that runs the trading strategy on historical data."""


class Backtest:
    def __init__(self, asset_a_data, asset_b_data, transaction_cost=0.01, date_range="1y"):
        self.transaction_cost = transaction_cost
        self.asset_a_data = asset_a_data
        self.asset_b_data = asset_b_data
        self.date_range = date_range
        self.backtest()

    @property
    def transaction_cost(self):
        return self.transaction_cost

    @transaction_cost.setter
    def transaction_cost(self, value):
        self.transaction_cost = value

    @property
    def asset_a_data(self):
        return self.asset_a_data

    @asset_a_data.setter
    def asset_a_data(self, data):
        self.asset_a_data = data

    @property
    def asset_b_data(self):
        return self.asset_b_data

    @asset_b_data.setter
    def asset_b_data(self, data):
        self.asset_b_data = data

    def backtest(self):
        pass

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
