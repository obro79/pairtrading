"""Strategy class that defines the trading strategy."""

from data import Data

class Strategy():
    def __init__(self, asset_a, asset_b, look_back_window=60,entry_threshold=2,exit_threshold=2):
        self.asset_a = asset_a
        self.asset_b = asset_b
        self.look_back_window = look_back_window
        self.data = Data(self.asset_a, self.asset_b, self.look_back_window)
        self.entry_threshold = entry_threshold
        self.exit_threshold = exit_threshold

    @property
    def asset_a(self):
        return self._asset_a

    @asset_a.setter
    def asset_a(self, value):
        self._asset_a = value

    @property
    def asset_b(self):
        return self._asset_b

    @asset_b.setter
    def asset_b(self, value):
        self._asset_b = value

    def get_next_action(self):
        """
        Summary: Returns the action the strategy should take next.
        Args: self
        Returns: action: int
        """
        pass

    def valid_pair(self):
        """
        Summary: Check if the pair of tickers will make be valid for pair trading.
        Args: self
        Returns: Boolean
        """
        asset_a_data = self.data.asset_1_data
        asset_b_data = self.data.asset_2_data
        is_cointegrated  = self.engle_granger_test(asset_1_data,asset_2_data)
        statistically_significant = self.p_value()
        correlation = self.correlation()
        return is_cointegrated and statistically_significant and correlation

    def engle_granger_test(self, asset_1_data, asset_2_data):
        """
        Summary: Return True if the two series are cointegrated.
        Args:  asset_1_data: pd of asset 1 data, asset_2_data: pd of asset 2 data
        Returns: boolean
        """
        pass

    def p_value(self, asset_1_data, asset_2_data):
        pass

    def correlation(self, asset_1_data, asset_2_data):
        """
        Summary: Return the correlation between the two series.
        Args: asset_1_data: pd of asset 1 data, asset_2_data: pd of asset 2 data
        Returns: the correlation between the two series.
        """
        pass
