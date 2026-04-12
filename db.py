import sqlite3

DB_NAME = "results.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_timestamp TEXT,
            time_dk TEXT,
            price REAL,
            anomaly INTEGER
        )
    """)

    conn.commit()
    conn.close()


def save_results(df):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO results (run_timestamp, time_dk, price, anomaly)
            VALUES (datetime('now'), ?, ?, ?)
        """, (
            str(row["TimeDK"]),
            float(row["DayAheadPriceDKK"]),
            int(row["anomaly"])
        ))

    conn.commit()
    conn.close()


def get_results():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, run_timestamp, time_dk, price, anomaly
        FROM results
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    results = []
    for row in rows:
        results.append({
            "id": row[0],
            "run_timestamp": row[1],
            "time_dk": row[2],
            "price": row[3],
            "anomaly": row[4]
        })

    return results