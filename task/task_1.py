import pandas
df = pandas.read_csv("week1_python_diagnostic_timeseries.csv")
print("\n")
print("Task 1")

print(f"Lines: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print(f"Column names: {df.columns[0]}, {df.columns[1]}, {df.columns[2]}, {df.columns[3]}, {df.columns[4]}, {df.columns[5]} {df.columns[6]}, {df.columns[7]}")

print("Column names    Data Type")
print(df.dtypes)

print("Date is not in datetime datatype")

print(f"Whether date is monotonic increasing: {df['date'].is_monotonic_increasing}")

print("Column names  Number of Missing Values")
print(df.isnull().sum())

print(f"Duplicated observations: {df.duplicated(subset=["date"]).sum()}")

print("Suspicious prices:")
print(df[(df["close"] > df["high"]) | (df["close"] < df["low"])])
print("Suspicious volumes:")
print(df[df["volume"] < 100])
print("Different date formats:")
print(df[df["date"].astype(str).str.contains("/")])
