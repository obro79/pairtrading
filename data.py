import yfinance as yf
import plotly.graph_objects as go
import matplotlib.pyplot as plt

def get_data(asset_1, asset_2, date_range):
    asset_1 = yf.Ticker(asset_1)
    asset_2 = yf.Ticker(asset_2)

    asset_1_data = asset_1.history(period=date_range)
    asset_2_data = asset_2.history(period=date_range)

    asset_1_data = asset_1_data.reset_index()
    asset_2_data = asset_2_data.reset_index()

    print(asset_2_data.columns)
    print(asset_1_data)

    return asset_1_data, asset_2_data

def create_chart(asset_1_data, asset_2_data, asset_1_name, asset_2_name):

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=asset_1_data['Date'], y=asset_1_data['Close'], mode="lines", name=asset_1_name))
    fig.add_trace(go.Scatter(x=asset_2_data['Date'], y=asset_2_data['Close'], mode="lines", name=asset_2_name))
    fig.update_layout(xaxis_title="Time", yaxis_title="Price")
    return fig


#TODO z-score

if __name__ == "__main__":
    get_data("AAPL", "MSFT","1y")