import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Energy_DE2025_Load_Orig.csv")

df['Time_clean'] = df['Time'].astype(str).str.replace(r'\s*\((CET|CEST)\)', '', regex=True)
df[['Start', 'End']] = df['Time_clean'].astype(str).str.split(' - ', expand=True)

df['Start'] = pd.to_datetime(df['Start'], dayfirst=True, errors='coerce')
df['End'] = pd.to_datetime(df['End'], dayfirst=True, errors='coerce')


# Convert numeric columns
df['Load Forecast'] = pd.to_numeric(df['Load Forecast'], errors='coerce')
df['Real Load'] = pd.to_numeric(df['Real Load'], errors='coerce')

# Calculate errors
df['Error_Forecasting_Load'] = df['Real Load'] - df['Load Forecast']
df['Error_For_Load_%'] = (df['Error_Forecasting_Load'] / df['Load Forecast']) * 100

#print(df.head())
df['Start'] = df['Start'].dt.strftime('%Y-%m-%dT%H:%M:%S')
df['End'] = df['End'].dt.strftime('%Y-%m-%dT%H:%M:%S')

df.to_csv(
    "Energy_DE2025_Load_Cleaned.csv",
    index=False,
    columns=['Time','Start', 'End', 'Real Load','Load Forecast', 'Error_Forecasting_Load', 'Error_For_Load_%']
)

# Plot
plt.figure(figsize=(10,5))
plt.plot(df['Start'], df['Load Forecast'], label='Forecast', linestyle='--')
plt.plot(df['Start'], df['Real Load'], label='Actual Load')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Value')
plt.title('Forecast vs Actual Load')
plt.show()
