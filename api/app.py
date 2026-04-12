from flask import Flask, jsonify, render_template
from data_ingestion.fetcher import fetch_prices
from preprocessing.preprocessing import preprocess
from model.anomaly_detector import detect_anomalies
from db import init_db, save_results, get_results


app = Flask(__name__)
init_db()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/prices")
def get_prices():
    # step 1: fetch data
    records = fetch_prices()
    
    # step 2: Preprocess
    df = preprocess(records)
    
    # step 3: Find anomalies
    df = detect_anomalies(df)

    save_results(df)

    
    # step 4: convert to json and return
    return jsonify(df.to_dict(orient="records"))

@app.route("/results")
def results():
    data = get_results()
    return jsonify(data)
    
    



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)