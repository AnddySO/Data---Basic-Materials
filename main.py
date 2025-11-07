import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Energy_DE2025_Load_Cleaned.csv")


fig, ax1 = plt.subplots(figsize=(12,6))

df['Real Load'] = pd.to_numeric(df['Real Load'], errors='coerce')
df['Start'] = pd.to_datetime(df['Start'], errors='coerce')

# Plot load and forecast
ax1.plot(df['Start'], df['Real Load'], label='Real Load', color='blue')
ax1.plot(df['Start'], df['Load Forecast'], label='Load Forecast', linestyle='--', color='orange')
ax1.set_xlabel('Time')
ax1.set_ylabel('Load (MW)')
ax1.legend(loc='upper left')

# Plot price on a second y-axis
ax2 = ax1.twinx()
ax2.plot(df['Start'], df['Price (EUR/Mwh)'], label='Price (EUR/Mwh)', color='green', alpha=0.6)
ax2.set_ylabel('Price (EUR/MWh)')
ax2.legend(loc='upper right')

plt.title('Real Load vs Forecast and Market Price')
plt.show()
