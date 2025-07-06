import yfinance as yf
import plotly.graph_objects as go
import matplotlib.pyplot as plt

class Data():
    def __init__(self, asset_1, asset_2, date_range):
        self.asset_1 = asset_1
        self.asset_2 = asset_2
        self.date_range = date_range
        self.asset_1_data, self.asset_2_data = fetch_data(self.asset_1, self.date_range), fetch_data(self.asset_2, self.date_range)

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
        asset = yf.Ticker(asset)
        asset = asset.history(period=date_range)
        asset = asset.reset_index()
        return asset

    def create_chart(asset_1_data, asset_2_data, asset_1_name, asset_2_name):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=asset_1_data['Date'], y=asset_1_data['Close'], mode="lines", name=asset_1_name))
        fig.add_trace(go.Scatter(x=asset_2_data['Date'], y=asset_2_data['Close'], mode="lines", name=asset_2_name))
        fig.update_layout(xaxis_title="Time", yaxis_title="Price")
        return fig
