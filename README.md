# Stock Ticker Chart & Table
[Alpha Vantage API](https://www.alphavantage.co/documentation/#dailyadj)

Daily limit of 25


# Starting server

## Create a virtual environment
```bash
python -m venv myenv
```

## Activate the virtual environment
```bash
# Windows
myenv\Scripts\activate

# Mac
source myenv/bin/activate
```

## Install packages
```bash
pip install -r requirements.txt
```

## Start API
```bash
uvicorn main:app --reload
```