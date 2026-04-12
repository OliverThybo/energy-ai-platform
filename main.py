from data_ingestion.fetcher import fetch_prices
from preprocessing.preprocessing import preprocess
from model.anomaly_detector import detect_anomalies

records = fetch_prices(limit=100)
df = preprocess(records)
df = detect_anomalies(df)

print(df[df["anomaly"] == True])
