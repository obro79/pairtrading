"""Porfolio class that stores current portfolio value and current holdings."""

class Portfolio:
    def __init__(self,initial_balance):
        self.total_value = initial_balance
        self.current_cash = initial_balance
        self.current_holdings = []

        @property
        def total_value(self):
            return self.current_cash + get_current_holdings_value(self)

        @property
        def current_cash(self):
            return self.current_cash

        @current_cash.setter
        def current_cash(self,cash):
            self.current_cash = cash

        @property
        def current_holdings(self):
            return self.current_holdings

        @current_holdings.setter
        def current_holdings(self,holdings):
            self.current_holdings = holdings

        def get_current_holdings_value(self):
            """
            Summary: Returns the value of the current holdings.
            Args: self
            Returns: current_holdings_value: float
            """

            pass