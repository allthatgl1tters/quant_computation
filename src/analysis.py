import pandas
import matplotlib.pyplot as plt
from pathlib import Path

def load_data(file_path):
    df=pandas.read_csv(file_path)
    df

def calculate_returns(df):
    df=df.copy()
    df["daily_return"] = df["close"].pct_change(fill_methode=None)
    df["market_return"] = df["market_close"].pct_change(fill_method=None)
    df["excess_return"] = ( df["daily_return"] - df["market_return"])
    return df