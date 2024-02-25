from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import requests
import os
import json


load_dotenv()

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)

stock_api_key = os.environ.get("STOCK_API_KEY")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/stocks/{stock_ticker}/daily")
def read_stock(stock_ticker: str):
    # Due to API rate limiting of 25 per day, using the example data from data.json file
    # url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_ticker}&apikey={stock_api_key}"
    # r = requests.get(url)
    # data = r.json()
    
    json_data = f"{stock_ticker}.json"
    with open(json_data, 'r') as file:
        data = json.load(file)

    print(data.get("Meta Data"))
    chart_data = transform_data_chart(data)
    table_data = transform_data_table(data)

    return { "chartData": chart_data, "tableData": table_data }

def transform_data_chart(input_data):
    time_series_data = input_data.get("Time Series (Daily)", {})

    transformed_data = {
        "labels": [],
        "datasets": [{"data": [], "label": []}]
    }

    for date, daily_data in time_series_data.items():
        transformed_data["labels"].append(date)
        # Append the closing price to the datasets
        transformed_data["datasets"][0]["data"].append(daily_data["4. close"])
    
    # FE renders it from start to finish as left to right, so reverse the data since it's a time series
    transformed_data["labels"].reverse()
    transformed_data["datasets"][0]["data"].reverse()

    return transformed_data

def transform_data_table(input_data):
    time_series_data = input_data.get("Time Series (Daily)", {})

    transformed_data = []

    for date, daily_data in time_series_data.items():
        volume = daily_data["6. volume"]
        formatted_volume = f"{int(volume):,}"
        transformed_data.append({
            "date": date,
            "open": daily_data["1. open"],
            "high": daily_data["2. high"],
            "low": daily_data["3. low"],
            "close": daily_data["4. close"],
            "volume": formatted_volume
        })
    
    return transformed_data