"""Trades class that stores trades."""
from trade import Trade


class Trades:
    def __init__(self) -> None:
        self.trades = []

    def add_trade(self, trade: Trade) -> None:
        self.trades.append(trade)

    @property
    def trades(self) -> list[Trade]:
        return self.trades
