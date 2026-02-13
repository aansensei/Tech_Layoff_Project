import yfinance as yf
import pandas as pd
import os

# target big tech stocks
tickers = ['META', 'AMZN', 'GOOGL', 'MSFT', 'AAPL']

# Downloading stock data
print("Downloading stock data...")
raw_data = yf.download(tickers, start="2020-01-01", end="2025-12-31")

if 'Adj Close' in raw_data.columns:
    data = raw_data['Adj Close']
else:
    print("Can not find 'Adj Close' column, using 'Close' instead.")
    data = raw_data['Close']

# Reset index to have 'Date' as a column
data = data.reset_index()

# FIX: Get the absolute path of the current script (src/get_stock_data.py)
current_script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct path: Go up one level from 'src' to project root, then into 'data/raw'
output_dir = os.path.join(current_script_dir, '..', 'data', 'raw')

# Create directory if it does not exist
os.makedirs(output_dir, exist_ok=True)

# Define full output path
output_path = os.path.join(output_dir, 'big_tech_stock_prices.csv')

# save to csv
data.to_csv(output_path, index=False)

print(f"Done! File is saved at: {os.path.abspath(output_path)}")
print(data.head())
