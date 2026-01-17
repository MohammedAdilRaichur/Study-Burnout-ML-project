import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report

df = pd.read_csv("data/raw_data.csv")

x = df.drop(["productivity_score","burnout_risk"],axis=1)
y = df["burnout_risk"]

x_train,x_test,y_train,y_test = train_test_split(
    x,y,test_size=0.2,random_state=42
    )
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

model = LogisticRegression()
model.fit(x_train_scaled,y_train)

y_pred = model.predict(x_test_scaled)

print("Accuracy: ",accuracy_score(y_test,y_pred))
print(classification_report(y_test,y_pred))

joblib.dump(model,"model/burnout_model.pkl")
joblib.dump(scaler,"model/scaler.pkl")
