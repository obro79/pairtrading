"""Stores the frontend of the app."""

import streamlit as st

from backtest import *
from data import Data

st.title("Pairs Trading Demo")
asset_1 = st.sidebar.text_input(key="asset_1", label="Asset 1", value="AAPL")
asset_2 = st.sidebar.text_input(key="asset_2", label="Asset 2", value="GOOG")
run_backtest = st.sidebar.button(label="Run Backtest")

date_range = str(st.sidebar.slider(label="Date Range (Years)", min_value=1, max_value=20)) + "y"

st.write(f"Asset 1: {asset_1}")
st.write(f"Asset 2: {asset_2}")
st.write(f"Data Range: {date_range}")

if run_backtest:
    st.write("Running backtest...")
    Data = Data(asset_1, asset_2, date_range)
    Backtest(Data.asset_1_data, Data.asset_2_data, )  ## just pass in data object?
