"""Data class that fetches historical data from Yahoo Finance."""

import plotly.graph_objects as go
import yfinance as yf


class Data():
    def __init__(self, asset_1, asset_2, date_range):
        self.asset_1 = asset_1
        self.asset_2 = asset_2
        self.date_range = date_range
        self.asset_1_data, self.asset_2_data = fetch_data(self.asset_1, self.date_range), fetch_data(self.asset_2,
                                                                                                     self.date_range)

    @property
    def asset_1(self):
        return self.asset_1

    @asset_1.setter
    def asset_1(self, value):
        self.asset_1 = value

    @property
    def asset_2(self):
        return self.asset_2

    @asset_2.setter
    def asset_2(self, value):
        self.asset_2 = value

    @property
    def date_range(self):
        return self.date_range

    @date_range.setter
    def date_range(self, value):
        self.date_range = value

    @property
    def asset_1_data(self):
        return self.asset_1_data

    @property
    def asset_2_data(self):
        return self.asset_2_data

    def fetch_data(asset, date_range):
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
