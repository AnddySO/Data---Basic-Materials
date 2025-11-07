import yfinance as yf
from datetime import datetime, timedelta

# Download oil price data (WTI Crude Oil)
# Using CL=F ticker which is the continuous futures contract for WTI Crude Oil
ticker = "CL=F"

# Calculate date range (last year)
end_date = datetime.now()
start_date = end_date - timedelta(days=365)

print(f"Downloading {ticker} data from {start_date.date()} to {end_date.date()}...")

# Download the data
asset_data = yf.download(
    ticker,
    start=start_date,
    end=end_date,
    interval="1d",
    progress=False
)

# Format the date index to the desired format
asset_data.index = asset_data.index.strftime('%Y-%m-%dT%H:%M:%S')

# Save to CSV
filename = "oil_prices_last_year.csv"
asset_data.to_csv(filename)

print(asset_data.tail())