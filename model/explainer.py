import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def explain_results(df):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    
    anomaly_count = int(df["anomaly"].sum())
    max_price = float(df["DayAheadPriceDKK"].max())
    min_price = float(df["DayAheadPriceDKK"].min())
    total = len(df)

    
    prompt = f"""
    You are an energy market analyst. Summarize this electricity price analysis in 3-4 simple sentences:
    - Total hours analyzed: {total}
    - Anomalies found: {anomaly_count}
    - Highest price: {max_price:.0f} DKK/MWh
    - Lowest price: {min_price:.0f} DKK/MWh
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content