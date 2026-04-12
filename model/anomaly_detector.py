from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    model = IsolationForest()

    model.fit(df[["DayAheadPriceDKK"]])

    predictions = model.predict(df[["DayAheadPriceDKK"]])

    df["anomaly"] = predictions == -1

    return df 


