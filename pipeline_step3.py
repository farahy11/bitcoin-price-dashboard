import requests
import pandas as pd
import sqlite3

DB_NAME = "crypto.db"


def fetch_bitcoin_data(days=1):
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        "vs_currency": "usd",
        "days": str(days)
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def create_price_dataframe(data):
    prices = data["prices"]

    df = pd.DataFrame(prices, columns=["timestamp_ms", "price_usd"])
    df["timestamp"] = pd.to_datetime(df["timestamp_ms"], unit="ms")
    df.set_index("timestamp", inplace=True)
    df.drop(columns=["timestamp_ms"], inplace=True)

    return df


def save_to_sqlite(df):
    conn = sqlite3.connect(DB_NAME)
    df.to_sql("bitcoin_prices", conn, if_exists="append", index=True)
    conn.close()

    print(f"✅ Stored {len(df)} rows into {DB_NAME}")


if __name__ == "__main__":
    data = fetch_bitcoin_data(days=1)
    df = create_price_dataframe(data)
    save_to_sqlite(df)

