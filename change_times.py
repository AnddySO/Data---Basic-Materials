import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Energy_DE2025_Load_Cleaned.csv")


df['Start'] = pd.to_datetime(df['Start'], errors='coerce')
df = df.set_index('Start')

df_hourly = df.resample('D').mean(numeric_only=True)

# df_hourly = df.resample('H').agg({
#     'Real Load': 'mean',
#     'Load Forecast': 'mean',
#     'Price (EUR/Mwh)': 'mean'
#     #'Sequence': 'last'  # keeps the last sequence in the hour
# })

#df_hourly.to_csv("Energy_DE2025_Load_Hourly.csv")
df_hourly.to_csv("Energy_DE2025_Load_Daily.csv")

fig, ax1 = plt.subplots(figsize=(12,6))

ax1.plot(df_hourly.index, df_hourly['Real Load'], label='Real Load', color='blue')
ax1.plot(df_hourly.index, df_hourly['Load Forecast'], label='Load Forecast', linestyle='--', color='orange')
ax1.set_xlabel('Time')
ax1.set_ylabel('Load (MW)')
ax1.legend(loc='upper left')

ax2 = ax1.twinx()
ax2.plot(df_hourly.index, df_hourly['Price (EUR/Mwh)'], label='Price (EUR/Mwh)', color='green', alpha=0.6)
ax2.set_ylabel('Price (EUR/MWh)')
ax2.legend(loc='upper right')

plt.title('Real Load vs Forecast and Market Price (Hourly)')
plt.show()