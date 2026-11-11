import pandas
cleaned_df = pandas.read_csv("cleaned_data.csv")

cleaned_df['daily_return'] = cleaned_df['close'].pct_change()

cleaned_df['rolling_mean_5'] = cleaned_df['close'].rolling(5).mean()
cleaned_df['rolling_mean_20'] = cleaned_df['close'].rolling(20).mean()
cleaned_df['rolling_std_20'] = cleaned_df['close'].rolling(20).std()

cleaned_df['market_return'] = cleaned_df['market_close'].pct_change()

cleaned_df["excess_return"] = (cleaned_df["daily_return"] - cleaned_df["market_return"])

cleaned_df.to_csv("cleaned_data_edited.csv", index=False)
