import requests

def fetch_bitcoin_data():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        "vs_currency": "usd",
        "days": "30"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error while calling the API:", e)
        return None


if __name__ == "__main__":
    data = fetch_bitcoin_data()
    if data:
        print("Keys returned:", data.keys())
        print("First 3 price points:", data["prices"][:3])

