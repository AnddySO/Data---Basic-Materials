import pandas as pd

#Clean and Standar the data

df = pd.read_csv("Energy_DE2025_Prices_Orig.csv")

df['Time'] = df['Time'].str.strip()
df['Sequence'] = df['Sequence'].str.strip()

# Find all Time values that have both Sequence 1 and 2
times_with_both = df.groupby('Time')['Sequence'].nunique()
times_with_both = times_with_both[times_with_both > 1].index

# Keep Sequence 2 where both exist, otherwise keep all others
filtered_df = df[
    ~((df['Time'].isin(times_with_both)) & (df['Sequence'].str.contains('Sequence 1')))
]

filtered_df.to_csv("filtered_data.csv", index=False)
