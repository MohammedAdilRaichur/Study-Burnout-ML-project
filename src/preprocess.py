import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

df = pd.read_csv("data/raw_data.csv")

x = df.drop(["productivity_score","burnout_risk"],axis=1)
y_reg = df["productivity_score"]
y_clf = df["burnout_risk"]

# Train-Test Split
x_train,x_test,y_reg_train,y_reg_test,y_clf_train,y_clf_test = train_test_split(
    x,y_reg,y_clf,test_size=0.2,random_state=42
    )

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

joblib.dump(scaler,"model/scaler.pkl")

print("Preprocessing Completed Successfully!")