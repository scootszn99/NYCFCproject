import pandas as pd
from pandas import DataFrame

# reading in the raw data
df = pd.read_csv("goalsadded.csv")
df2 = pd.read_csv("salaries.csv")

# dropping phantom unnamed columns
df = df.drop(df.columns[[0]], axis=1)
df2 = df2.drop(df2.columns[[0]], axis=1)

# filtering salary data for only September dates to have one entry per player each season
df2['Date'] = pd.to_datetime(df2['Date'], errors='coerce')
df2 = df2[df2['Date'].dt.month == 9]

# merging goals added and salary data
df = pd.merge(df, df2, how="left", on=["Player", "Season"])

# dropping redundant columns and renaming
df = df.drop(['Team_y', 'Position_y', 'Date'], axis=1)
df = df.rename(columns={"Team_x": "Team", "Position_x": "Position"})

# exporting ready to use data
df.to_csv('exportedmetrics.csv', index=False)
