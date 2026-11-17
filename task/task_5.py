import pandas

df = pandas.read_csv("data/processed/cleaned_data_edited.csv")
df["date"] = pandas.to_datetime(df["date"])

#Question 1
print("\nQuestion 1: ")
print(f"Mean: {df["daily_return"].mean() * 100:.4f}%")
print(f"Median: {df["daily_return"].median() * 100:.4f}%")
print(f"Standard Deviation: {df["daily_return"].std() * 100:.4f}%")
print(f"Minimum: {df["daily_return"].min() * 100:.4f}%")
print(f"Maximum: {df["daily_return"].max() * 100:.4f}%")

#Question 2
correlation = df["daily_return"].corr(df["market_return"])
print("\nQuestion 2: ")
print(f"Correlation: {correlation:.4f}")

#Question 3
middle = len(df)//2
first_half = df.iloc[:middle]
second_half = df.iloc[middle:]

print("\nQuestion 3: \nFirst 50%")
print(f"Average Return: {first_half["daily_return"].mean()*100:.4f}%")
print(f"Volatility: {first_half["daily_return"].std()*100:.4f}%")
print(f"Correlation: {first_half["daily_return"].corr(first_half["market_return"]):.4f}")
print("\nLast 50%")
print(f"Average Return: {second_half["daily_return"].mean()*100:.4f}%")
print(f"Volatility: {second_half["daily_return"].std()*100:.4f}%")
print(f"Correlation: {second_half["daily_return"].corr(first_half["market_return"]):.4f}")

#Question 4
df["abs_return"] = df["daily_return"].abs()
top5 = df.nlargest(5, "abs_return")
print("\nQuestion 4:")
print(top5[["date","daily_return","abs_return"]])
