import pandas
df = pandas.read_csv("week1_python_diagnostic_timeseries.csv")
cleaned_df = df.copy()

cleaned_df['date']=pandas.to_datetime(cleaned_df['date'], format="mixed")
cleaned_df = cleaned_df.sort_values(by='date')

duplicates = cleaned_df[cleaned_df.duplicated(subset=['date'], keep='first')]
print("Duplicated values:")
print(duplicates)
print()

missing = cleaned_df.isnull().sum()
#clean_df = cleaned_df.dropna(subset='close')
print("Missing values:")
print(missing)
print()


abnormalprice = cleaned_df[(cleaned_df["close"] > cleaned_df["high"]) | (cleaned_df["close"] < cleaned_df["low"])]
abnormalvolume = cleaned_df[cleaned_df["volume"] < 100]
abnormalmarket = cleaned_df[cleaned_df["market_close"] <= 0]
print("Abnormal prices:")
print(abnormalprice)
print()
print("Abnormal volumes:")
print(abnormalvolume)
print()
print("Abnormal market prices:")
print(abnormalmarket)
print()

cleaned_df.to_csv("cleaned_data.csv", index=False)
