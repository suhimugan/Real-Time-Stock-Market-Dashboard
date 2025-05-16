# data_cleaning.py (updated for daily data)

import pandas as pd

def clean_stock_data(raw_json):
    """Converts raw daily API response into a clean DataFrame."""
    time_series = raw_json.get("Time Series (Daily)", {})
    if not time_series:
        print("No time series data found.")
        return pd.DataFrame()
    
    df = pd.DataFrame.from_dict(time_series, orient="index")
    df.rename(columns={
        '1. open': 'Open',
        '2. high': 'High',
        '3. low': 'Low',
        '4. close': 'Close',
        '5. volume': 'Volume'
    }, inplace=True)
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    return df
