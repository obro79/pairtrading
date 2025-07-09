"""
Trivial “smoke test” to prove the Backtest class can be instantiated.

It feeds Backtest the smallest possible dummy data-frames so we avoid
hitting Yahoo Finance or any real strategy logic.
"""

import pandas as pd

import CONSTANTS
from backtest import Backtest
from date_range import DateRange


def _dummy_price_df():
    """Two-row DataFrame with the bare columns Backtest expects."""
    dates = pd.date_range("2024-01-01", periods=2, freq="D")
    return pd.DataFrame(
        {
            "Date": dates,
            "Close": [100.0, 101.0],
        }
    )


def test_backtest_instantiation():
    # Minimal DateRange: two consecutive days
    dr = DateRange("2024-01-01", "2024-01-02")

    # Dummy price data for both legs of the pair
    dummy_df_a = _dummy_price_df()
    dummy_df_b = _dummy_price_df()

    # Instantiate Backtest – we ignore strategy logic here
    bt = Backtest(
        asset_a_data=dummy_df_a,
        asset_b_data=dummy_df_b,
        transaction_cost=CONSTANTS.COMMISSION,
        start_date=dr.start_date.date().isoformat(),
        end_date=dr.end_date.date().isoformat(),
    )

    assert bt is not None
