import requests
import pandas as pd


def fetch_bitcoin_data(days=30):
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

    # Convert timestamp from milliseconds to datetime
    df["timestamp"] = pd.to_datetime(df["timestamp_ms"], unit="ms")

    # Set timestamp as index
    df.set_index("timestamp", inplace=True)

    # Drop raw timestamp column
    df.drop(columns=["timestamp_ms"], inplace=True)

    return df


if __name__ == "__main__":
    raw_data = fetch_bitcoin_data(days=30)
    df = create_price_dataframe(raw_data)
    print(df.head())

