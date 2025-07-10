"""Trades class that stores trades."""
from trade import Trade


class Trades:
    def __init__(self) -> None:
        self._trades = []

    def add_trade(self, trade: Trade) -> None:
        self._trades.append(trade)

    @property
    def trades(self) -> list[Trade]:
        return self._trades
