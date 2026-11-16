import pandas

df = pandas.read_csv("data/processed/cleaned_data_edited.csv")
df["date"] = pandas.to_datetime(df["date"])

#Question 1
print("Question 1: Daily Return Statistics")
print(f"Mean: {df["daily_return"].mean() * 100:.4f}%")
print(f"Median: {df["daily_return"].median() * 100:.4f}%")
print(f"Standard Deviation: {df["daily_return"].std() * 100:.4f}%")
print(f"Minimum: {df["daily_return"].min() * 100:.4f}%")
print(f"Maximum: {df["daily_return"].max() * 100:.4f}%")
