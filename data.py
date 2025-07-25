"""Data class that fetches historical data from Yahoo Finance."""

from dataclasses import dataclass, field

import pandas as pd
import plotly.graph_objects as go
import yfinance as yf
from numpy.f2py.auxfuncs import throw_error

from date_range import DateRange


@dataclass
class Data:
    asset_1: str
    asset_2: str
    date_range: DateRange
    asset_1_data: pd.DataFrame = field(init=False)
    asset_2_data: pd.DataFrame = field(init=False)

    def __post_init__(self):
        # Fetch data for both assets after initialization
        self.asset_1_data = self.fetch_data(self.asset_1, self.date_range)
        self.asset_2_data = self.fetch_data(self.asset_2, self.date_range)

    def fetch_data(self, asset: str, date_range: DateRange) -> pd.DataFrame:
        """
        Summary: fetcher for historical data for the given asset and date range.
        Args: datarange: str, date range for the data to be fetched.
        Returns: asset_data: pd of asset data,
        """
        asset = yf.Ticker(asset)
        asset = asset.history(period=date_range)
        asset = asset.reset_index()
        return asset

    def create_chart(self):
        """
        Summary: Creates a plotly chart of the historical data for the two assets.
        Args: self
        Returns: plotly chart of the historical data for the two assets.
        """
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(x=self.asset_1_data['Date'], y=self.asset_1_data['Close'], mode="lines", name=self.asset_1))
        fig.add_trace(
            go.Scatter(x=self.asset_2_data['Date'], y=self.asset_2_data['Close'], mode="lines", name=self.asset_2))
        fig.update_layout(xaxis_title="Time", yaxis_title="Price")
        return fig

    def get_price_on_date(self, ticker: str, date: DateRange) -> float:
        """
        Summary: returns the price of the given ticker on the given date.
        Args: ticker: str, date: str
        Returns: price: float
        """
        if ticker != self.asset_1 or ticker != self.asset_2:
            throw_error("Ticker not in data")
        elif ticker == self.asset_1:
            return self.asset_1_data[self.asset_1_data['Date'] == date]['Close'].values[0]
        else:
            return self.asset_2_data[self.asset_2_data['Date'] == date]['Close'].values[0]
