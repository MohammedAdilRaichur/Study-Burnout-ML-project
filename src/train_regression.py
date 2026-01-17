import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,r2_score

df = pd.read_csv("data/raw_data.csv")

x = df.drop(["productivity_score","burnout_risk"],axis=1)
y = df["productivity_score"]

x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.2,random_state=42
)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

model = RandomForestRegressor(
    n_estimators=150,
    random_state=42
)

model.fit(x_train_scaled,y_train)

y_pred = model.predict(x_test_scaled)

print("Mean Absolute Error: ",mean_absolute_error(y_test,y_pred))
print("R2 score: ",r2_score(y_test,y_pred))

joblib.dump(model, "model/productivity_model.pkl")
joblib.dump(scaler, "model/scaler.pkl")