import pandas
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path

df = pandas.read_csv("cleaned_data_edited.csv")
df["date"] = pandas.to_datetime(df["date"])
df = df.sort_values("date").copy()

print(df.columns.tolist())
print(df.head())