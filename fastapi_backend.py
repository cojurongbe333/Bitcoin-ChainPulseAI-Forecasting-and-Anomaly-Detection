
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="ChainPulseAI Risk API")

# Load model
model = joblib.load('../models/risk_model.pkl')

# Define input schema
class RiskInput(BaseModel):
    open: float
    close: float
    high: float
    low: float
    volume: float
    avg_sentiment: float
    tx_spike: int
    daily_return: float
    volatility: float

@app.post("/predict/")
def predict_risk(data: RiskInput):
    input_df = pd.DataFrame([data.dict()])
    prediction = model.predict(input_df)[0]
    return {"risk_prediction": int(prediction)}
