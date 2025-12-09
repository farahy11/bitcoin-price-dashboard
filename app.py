import sqlite3
import pandas as pd
import streamlit as st

DB_NAME = "crypto.db"


def load_data():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql("SELECT * FROM bitcoin_prices", conn, parse_dates=["timestamp"])
    conn.close()
    df.set_index("timestamp", inplace=True)
    return df


def main():
    st.title("Bitcoin Price Dashboard 🪙")
    st.write("CoinGecko → SQLite → Streamlit")

    df = load_data()

    st.subheader("Latest prices")
    st.dataframe(df.tail(10))

    st.subheader("Bitcoin price over time")
    st.line_chart(df["price_usd"])

    st.subheader("Summary statistics")
    st.write(df["price_usd"].describe())


if __name__ == "__main__":
    main()

