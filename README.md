📊 Bitcoin Price Data Pipeline & Dashboard

End-to-end data pipeline that extracts real-time Bitcoin price data from a public API, processes it using Python and Pandas, stores it in a local SQLite database, and visualises trends using a Streamlit dashboard.

## Architecture Overview

This project follows a simple end-to-end data pipeline architecture:

API → Data Processing → Storage → Visualisation

- Data is extracted from a public cryptocurrency API
- Processed and cleaned using Python and Pandas
- Stored locally in a SQLite database
- Visualised through an interactive Streamlit dashboard

### Project Goals

- Work with a real public API

- Practice data transformation

- Store data persistently

- Present insights in a simple dashboard

## Problem Statement

### Situation
Public cryptocurrency APIs provide large volumes of raw data that are not immediately usable for analysis.

### Task
Design and build a small data pipeline that:
- Collects live Bitcoin price data
- Cleans and structures the data
- Stores it for reuse
- Visualises trends over time

### Action
- Used Python to call the CoinGecko API
- Transformed raw JSON data using Pandas
- Stored processed data in a SQLite database
- Built a Streamlit dashboard to display prices and trends

### Result
- Successfully built a working end-to-end pipeline
- Stored 287+ historical price records, enabling trend analysis over time
- Created a reusable dashboard for historical analysis
- Improved understanding of real-world data engineering workflows



## Architecture & Data Flow

CoinGecko API  
↓  
Python (requests)  
↓  
Pandas (data cleaning & transformation)  
↓  
SQLite (persistent storage)  
↓  
Streamlit (dashboard visualisation)


## Pipeline Steps

### Step 1: Extract

Fetches Bitcoin price data from the CoinGecko API

Handles API errors gracefully

### Step 2: Transform

Converts raw JSON into a Pandas DataFrame

Converts timestamps to readable datetime format

Cleans and structures the dataset

### Step 3: Load

Stores transformed data into a SQLite database  
Enables historical tracking and querying  

SQLite was chosen as a lightweight database to persist historical price data locally and enable simple querying without additional infrastructure.

### Step 4: Visualise

Reads data from SQLite

Displays latest prices, trends, and summary statistics in Streamlit

## Technology Stack

| Category            | Tool                          |
|---------------------|-------------------------------|
| Language            | Python                        |
| Data Processing     | Pandas                        |
| API                 | CoinGecko (Public API)        |
| Database            | SQLite                        |
| Visualisation       | Streamlit                     |
| Environment         | Virtualenv                    |


## Repository Structure
bitcoin-price-dashboard/
│
├── pipeline_step1.py   # API data extraction
├── pipeline_step2.py   # Data transformation
├── pipeline_step3.py   # Load data into SQLite
├── app.py              # Streamlit dashboard
├── crypto.db           # SQLite database
├── requirements.txt    # Dependencies
└── README.md



## How to Run the Project
# Activate virtual environment
source env/bin/activate

# Run the data pipeline
python pipeline_step3.py

# Launch the dashboard
streamlit run app.py


## Example Output
Latest Bitcoin prices displayed in a table

Line chart showing price trends over time

Summary statistics (min, max, average price)

## Future Improvements
Automate daily data collection (cron / scheduler)

Add multiple cryptocurrencies

Prevent duplicate timestamp inserts

Move from SQLite to PostgreSQL

Deploy Streamlit dashboard online

## Why This Project?

- Demonstrates understanding of end-to-end data pipelines
- Uses real-world, continuously changing data
- Focuses on core data engineering concepts without over-engineering
- Designed to be simple, reproducible, and easy to explain


