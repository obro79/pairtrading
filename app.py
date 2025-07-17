"""Stores the frontend of the app."""

from backtest import *

# st.title("Pairs Trading Demo")
# asset_1 = st.sidebar.text_input(key="asset_1", label="Asset 1", value="AAPL")
# asset_2 = st.sidebar.text_input(key="asset_2", label="Asset 2", value="GOOG")
# run_backtest = st.sidebar.button(label="Run Backtest")
#
# date_range = str(st.sidebar.slider(label="Date Range (Years)", min_value=1, max_value=20)) + "y"
#
# st.write(f"Asset 1: {asset_1}")
# st.write(f"Asset 2: {asset_2}")
# st.write(f"Data Range: {date_range}")
#
# if run_backtest:
#     st.write("Running backtest...")
#     Data = Data(asset_1, asset_2, date_range)
#     Backtest(Data.asset_1_data, Data.asset_2_data, )  ## just pass in data object?

if __name__ == "__main__":
    import yfinance as yf
    import pandas as pd
    from datetime import datetime

    aapl = yf.download("AAPL", start="2024-01-01", end="2024-03-01")
    msft = yf.download("MSFT", start="2024-01-01", end="2024-03-01")

    bt = Backtest(asset_a_data=aapl, asset_b_data=msft,
                  start_date="2024-01-01", end_date="2024-03-01")
    print("NAV points:", len(bt._nav_history))
    print("Last NAV:", list(bt._nav_history.values())[-1])
