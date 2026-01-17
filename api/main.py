from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="Study Productivity & Burnout API")

# ✅ CORS MUST be added immediately after app creation
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://localhost:3000",
    ],
    allow_credentials=False,  # MUST be False
    allow_methods=["*"],      # includes OPTIONS
    allow_headers=["*"],
)


# Load models
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
        data.consistency_score
    ]])

    features_scaled = scaler.transform(features)

    productivity = productivity_model.predict(features_scaled)[0]
    burnout = burnout_model.predict(features_scaled)[0]

    return {
        "productivity_score": round(float(productivity), 2),
        "burnout_risk": "Yes" if burnout == 1 else "No"
    }
