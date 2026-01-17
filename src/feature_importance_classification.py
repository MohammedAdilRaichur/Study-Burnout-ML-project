import joblib
import pandas as pd

model = joblib.load("model/burnout_model.pkl")

features = [
    "study_hours_per_day",
    "sleep_hours",
    "screen_time_hours",
    "breaks_per_day",
    "stress_level",
    "physical_activity",
    "consistency_score",
]

coefficients = model.coef_[0]

df = pd.DataFrame({
    "feature": features,
    "coefficient": coefficients
}).sort_values(by="coefficient",ascending=False)

print(df)