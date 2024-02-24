# Start server

## Create a virtual environment
python -m venv myenv

## Activate the virtual environment
myenv\Scripts\activate

## Install packages
pip install -r requirements.txt

## Start API
uvicorn main:app --reload