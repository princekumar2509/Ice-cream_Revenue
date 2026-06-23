import numpy as np
import pandas as pd
import os

os.makedirs("data", exist_ok=True)
np.random.seed(42)
n = 500

temperature = np.random.normal(30, 5, n)
humidity = np.random.uniform(30, 80, n)
promotion = np.random.binomial(1, 0.3, n)
footfall = np.random.poisson(80, n)
avg_price = np.random.uniform(1.5, 4.0, n)

# Revenue formula
revenue = (
    20 + (temperature - 20) * 2.5
    + promotion * 15
    + (footfall - 80) * 0.5
    + np.random.normal(0, 15, n)
) * avg_price/2

df = pd.DataFrame({
    "temperature": np.round(temperature,2),
    "humidity": np.round(humidity,2),
    "promotion": promotion,
    "footfall": footfall,
    "avg_price": np.round(avg_price,2),
    "revenue": np.round(revenue,2)
})

df.to_csv("data/icecream_data.csv", index=False)
print("✅ Dataset saved to data/icecream_data.csv")
