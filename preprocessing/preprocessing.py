import pandas as pd


def preprocess(records):
    df = pd.DataFrame(records)

    df = df[["TimeDK", "DayAheadPriceDKK"]]

    
    df["TimeDK"] = pd.to_datetime(df["TimeDK"])

    
    df = df.sort_values("TimeDK").reset_index(drop=True)

    return df
