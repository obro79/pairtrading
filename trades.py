class Trades:
    def __init__(self):
        self.trades = []

    def add_trade(self, trade):
        self.trades.append(trade)


    @property
    def trades(self):
        return self.trades