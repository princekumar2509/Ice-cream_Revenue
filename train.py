import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

os.makedirs("models", exist_ok=True)

df = pd.read_csv("data/icecream_data.csv")

X = df.drop("revenue", axis=1)
y = df["revenue"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", RandomForestRegressor(n_estimators=200, random_state=42))
])

pipe.fit(X_train, y_train)
print("✅ Model trained. Score:", pipe.score(X_test, y_test))

joblib.dump(pipe, "models/revenue_model.pkl")
print("✅ Model saved to models/revenue_model.pkl")
