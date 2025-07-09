"""Strategy class that defines the trading strategy."""

import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import coint

import CONSTANTS
import actions
from data import Data


class Strategy():
    def __init__(self, asset_a: str, asset_b: str, look_back_window=CONSTANTS.LOOK_BACK_WINDOW,
                 entry_threshold=CONSTANTS.ENTRY_THRESHOLD, exit_threshold=CONSTANTS.EXIT_THRESHOLD,
                 corr_threshold=CONSTANTS.CORR_THRESHOLD, coint_p=CONSTANTS.COINT_P,
                 max_half_life=CONSTANTS.MAX_HALF_LIFE) -> None:
        self.asset_a = asset_a
        self.asset_b = asset_b
        self.look_back_window = look_back_window
        self.data = Data(self.asset_a, self.asset_b, self.look_back_window)
        self.entry_threshold = entry_threshold
        self.exit_threshold = exit_threshold
        self.corr_threshold = corr_threshold
        self.coint_p = coint_p
        self.max_half_life = max_half_life

    @property
    def asset_a(self) -> pd.DataFrame:
        return self._asset_a

    @asset_a.setter
    def asset_a(self, value: float) -> None:
        self._asset_a = value

    @property
    def asset_b(self) -> pd.DataFrame:
        return self._asset_b

    @asset_b.setter
    def asset_b(self, value: float) -> None:
        self._asset_b = value

    def get_next_action(self):
        """
        Summary: Returns the action the strategy should take next.
        Args: self
        Returns: action: int
        """
        A, B = self._merge_closes(self.data.asset_1_data,
                                  self.data.asset_2_data)
        spread = A - B
        mu = spread.mean()
        sigma = spread.std(ddof=0)
        z = (spread.iloc[-1] - mu) / sigma

        if z >= self.entry_threshold:
            return actions.LONG_B_SHORT_A
        elif z <= -self.exit_threshold:
            return actions.LONG_A_SHORT_B
        elif abs(z) < self.exit_threshold:
            return actions.HOLD
        else:
            return actions.EXIT  ## TODO only exit when in position/ reorder

    def valid_pair(self) -> bool:
        """
        Summary: Check if the pair of tickers will make be valid for pair trading.
        Args: self
        Returns: Boolean
        """
        asset_a_data = self.data.asset_1_data
        asset_b_data = self.data.asset_2_data
        asset_a_data, asset_b_data = self._merge_closes(asset_a_data, asset_b_data)
        is_cointegrated = self._is_cointegrated(asset_a_data, asset_b_data)
        is_stably_correlated = self._is_stably_correlated(asset_a_data, asset_b_data)
        has_short_half_life = self._has_short_half_life(asset_a_data, asset_b_data)
        return is_cointegrated and is_stably_correlated and has_short_half_life

    def _is_cointegrated(self, asset_1_data, asset_2_data) -> bool:
        """
        Summary: Return True if the two series are cointegrated.
        Args:  asset_1_data: pd of asset 1 data, asset_2_data: pd of asset 2 data
        Returns: boolean
        """
        score, p_value, crit_vals = coint(asset_1_data, asset_2_data)
        cv_5pct = crit_vals[1]

        return score < cv_5pct and p_value < self.coint_p

    def _is_stably_correlated(self, asset_1_data, asset_2_data) -> bool:
        """
        Summary: Return the correlation between the two series.
        Args: asset_1_data: pd of asset 1 data, asset_2_data: pd of asset 2 data
        Returns: the correlation between the two series.
        """
        rolling = asset_1_data.rolling(self.look_back_window).corr(asset_2_data)
        stable_corr = rolling.min()
        return stable_corr.mean() > self.corr_threshold

    def _has_short_half_life(self, asset_1_data, asset_2_data) -> bool:
        """
        Summary: returns true if the deviation from the long term mean reverts to half under the max_half_life.
        Args: asset_1_data: pd of asset 1 data, asset_2_data: pd of asset 2 data
        Returns: boolean
        """
        spread = asset_1_data - asset_2_data
        lagged = spread.shift(1).fillna(method='bfill')
        delta = spread - lagged
        phi = sm.OLS(delta, sm.add_constant(lagged)).fit().params[1]
        if phi <= 0 or phi >= 1:
            return False
        half_life = -np.log(2) / np.log(phi)
        return half_life <= self.max_half_life

    def _merge_closes(self, asset_1_data: pd.DataFrame, asset_2_data: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
        """
        Summary: Merges the two dataframes on the Close column ensures the two series are aligned.
        Args: asset_1_data: pd of asset 1 data, asset_2_data: pd of asset 2 data
        Returns: asset_1_data, asset_2_data: pd of asset 1 data, asset 2 data, aligned on Close.
        """

        df = (
            asset_1_data['Close'].rename('A')
            .to_frame()
            .join(asset_2_data['Close'].rename('B'), how='inner')
            .dropna()
        )
        return df['A'], df['B']
