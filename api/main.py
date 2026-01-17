from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="Study Productivity & Burnout API")

productivity_model = joblib.load("model/productivity_model.pkl")
burnout_model = joblib.load("model/burnout_model.pkl")
scaler = joblib.load("model/scaler.pkl")

class StudentData(BaseModel):
    study_hours_per_day: float
    sleep_hours: float
    screen_time_hours: float
    breaks_per_day: int
    stress_level: int
    physical_activity: int
    consistency_score: int

@app.post("/predict")
def predict(data: StudentData):
    features = np.array([[
        data.study_hours_per_day,
        data.sleep_hours,
        data.screen_time_hours,
        data.breaks_per_day,
        data.stress_level,
        data.physical_activity,
        data.consistency_score,
    ]])

    features_scaled = scaler.transform(features)

    productivity = productivity_model.predict(features_scaled)[0]
    burnout = burnout_model.predict(features_scaled)[0]

    return{
        "Productivity_Score": round(float(productivity),2),
        "Burnout_Risk": "Yes" if burnout == 1 else "No"
    }