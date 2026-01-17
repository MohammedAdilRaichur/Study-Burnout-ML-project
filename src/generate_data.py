import pandas as pd
import numpy as np

np.random.seed(42)
n_samples = 1000

def round_half(x):
    return np.round(x * 2) / 2

data = {
    "study_hours_per_day": round_half(np.random.uniform(1, 10, n_samples)),
    "sleep_hours": round_half(np.random.uniform(4, 9, n_samples)),
    "screen_time_hours": round_half(np.random.uniform(2, 12, n_samples)),
    "breaks_per_day": np.random.randint(1, 8, n_samples),
    "stress_level": np.random.randint(1, 11, n_samples),
    "physical_activity": np.random.randint(0, 121, n_samples),
    "consistency_score": np.random.randint(1, 11, n_samples),
}

df = pd.DataFrame(data)

# Productivity score (single column)
df["productivity_score"] = (
    df["study_hours_per_day"] * 10
    + df["sleep_hours"] * 8
    - df["screen_time_hours"] * 4
    + df["physical_activity"] * 0.2
    + df["consistency_score"] * 5
)

df["productivity_score"] = df["productivity_score"].round().clip(0, 100)

# Burnout risk
df["burnout_risk"] = np.where(
    (df["sleep_hours"] < 6) & (df["stress_level"] > 7), 1, 0
)

df.to_csv("data/raw_data.csv", index=False)
print("Dataset generated successfully!")
