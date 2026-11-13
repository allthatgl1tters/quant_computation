import pandas
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path

data_file = Path("data/cleaned_data_edited.csv")
df = pandas.read_csv(data_file)
Path("figures").mkdir(exist_ok=True)
df["date"]=pandas.to_datetime(df["date"])
df=df.sort_values("date")

#Figure 1
plt.figure(figsize=(10,5))
plt.plot(df["date"], df["close"])
axes=plt.gca()
axes.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
axes.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
plt.title("Asset Close Price over Time")
plt.xticks(rotation=45)
plt.xlabel("Date")
plt.ylabel("Close Price / $")
plt.savefig("figures/figure_1.png", dpi=300)

#Figure 2
plt.figure(figsize=(10,5))
plt.plot(df["date"], df["daily_return"]*100)
axes=plt.gca()
axes.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
axes.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
plt.axhline(0, color="gray", linestyle="--")
plt.title("Daily Return over Time")
plt.xlabel("Date")
plt.ylabel("Daily return / %")
plt.xticks(rotation=45)
plt.savefig("figures/figure_2.png", dpi=300)

#Figure 3
plt.figure(figsize=(10, 5))
plt.hist(df["daily_return"].dropna()*100, bins=30)
plt.title("Distribution of Daily Returns")
plt.xlabel("Daily Return / %")
plt.ylabel("Frequency")
plt.savefig("figures/figure_3.png", dpi=300)

#Figure 4
comparison = df[["daily_return", "market_return"]].dropna()
plt.figure(figsize=(10,5))
plt.scatter(comparison["market_return"]*100,comparison["daily_return"]*100, alpha=0.4)
plt.title("Asset Return vs. Market Return")
plt.xlabel("Market Return / %")
plt.ylabel("Asset Return / %")
plt.savefig("figures/figure_4.png", dpi=300)
