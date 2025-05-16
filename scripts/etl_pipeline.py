# etl_pipeline.py

from api_fetch import fetch_stock_data
from data_cleaning import clean_stock_data
import os

# Create a 'data' folder if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")

# List of stock symbols to track
symbols = ["AAPL", "MSFT", "GOOGL"]

# Loop through each symbol, get data, clean it, and save it
for symbol in symbols:
    print(f"Processing {symbol}...")
    raw_data = fetch_stock_data(symbol, full=True)
    if raw_data:
        df = clean_stock_data(raw_data)
        if not df.empty:
            file_path = f"data/{symbol}_data.csv"
            df.to_csv(file_path)
            print(f"{symbol} data saved to {file_path}")
        else:
            print(f"Skipping {symbol} due to empty data.")
    else:
        print(f"Failed to fetch data for {symbol}")
