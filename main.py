from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
    stock_api_key = os.environ.get("STOCK_API_KEY")
    return {"Hello": "World"}

@app.get("/stocks/{stock_ticker}/history")
def read_stock(stock_ticker: str):
    return {"stock_ticker": stock_ticker}