import pandas as pd
import joblib
import matplotlib.pyplot as plt

model = joblib.load("model/productivity_model.pkl")

features = [
    "study_hours_per_day",
    "sleep_hours",
    "screen_time_hours",
    "breaks_per_day",
    "stress_level",
    "physical_activity",
    "consistency_score",
]

importance = model.feature_importances_

df = pd.DataFrame({
    "feature": features,
    "importance": importance
}).sort_values(by="importance",ascending=False)

print(df)

plt.barh(df["feature"],df["importance"])
plt.gca().invert_yaxis()
plt.title("Feature importance - Productivity Score")
plt.show()