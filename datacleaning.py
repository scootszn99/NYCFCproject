import pandas as pd
from pandas import DataFrame
import numpy as np

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

# adjusting for players that switch to different team mid-season for logo purposes
df[['Team', 'Team 2']] = df['Team'].str.split(', ', 1, expand=True)
df = df.replace(r'^\s*$', np.nan, regex=True)

# exporting ready to use data
df.to_csv('exportedmetrics.csv', index=False, encoding='utf-8-sig')
