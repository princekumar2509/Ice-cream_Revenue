import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Page config
st.set_page_config(page_title="🍦 Ice-cream Revenue Predictor", layout="centered")

# Add background style
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #fceabb, #f8b500);
        color: #333;
        font-family: "Trebuchet MS", sans-serif;
    }
    .title {
        text-align: center;
        color: #6f1d1b;
        font-size: 36px;
        font-weight: bold;
    }
    .prediction-card {
        background: #fff7e6;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="title">🍦 Ice-cream Revenue Predictor</h1>', unsafe_allow_html=True)
st.write("Enter shop, weather, and flavor details to predict your expected daily revenue.")

# Load model
model = joblib.load("models/revenue_model.pkl")

# Inputs
with st.form("inputs"):
    col1, col2 = st.columns(2)

    with col1:
        temperature = st.number_input("🌡️ Temperature (°C)", 10.0, 45.0, 30.0)
        humidity = st.slider("💧 Humidity (%)", 0, 100, 50)
        footfall = st.number_input("🚶 Estimated Footfall", 0, 500, 80)
        avg_price = st.number_input("💵 Avg item price (USD)", 0.5, 10.0, 2.5)

    with col2:
        promotion = st.radio("📢 Promotion running?", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
        flavor = st.selectbox("🍨 Ice-cream Flavor", ["Vanilla", "Chocolate", "Strawberry", "Mango", "Mixed"])
        cup_cone_ratio = st.slider("🍧 Cup vs Cone ratio (Cup %)", 0, 100, 50)
        toppings = st.radio("🍫 Toppings offered?", ["No", "Yes"])

    submitted = st.form_submit_button("🔮 Predict Revenue")

if submitted:
    # Encode flavor into numbers (simple encoding)
    flavor_map = {"Vanilla":0, "Chocolate":1, "Strawberry":2, "Mango":3, "Mixed":4}
    toppings_val = 1 if toppings == "Yes" else 0

    X = pd.DataFrame([{
        "temperature": temperature,
        "humidity": humidity,
        "promotion": promotion,
        "footfall": footfall,
        "avg_price": avg_price,
        "flavor": flavor_map[flavor],
        "cup_cone_ratio": cup_cone_ratio,
        "toppings": toppings_val
    }])

    # Since the current model doesn’t know flavor/cup/toppings,
    # we fake their influence for now (just for demo).
    base_pred = model.predict(X[["temperature","humidity","promotion","footfall","avg_price"]])[0]
    extra = (flavor_map[flavor] * 5) + (cup_cone_ratio * 0.2) + (toppings_val * 10)
    prediction = base_pred + extra

    st.markdown(
        f"""
        <div class="prediction-card">
            <h2>💰 Predicted Revenue: <span style="color:#d62828">${prediction:,.2f}</span></h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Bonus: Show how temperature affects revenue
    temps = np.linspace(15, 40, 10)
    preds = [model.predict(pd.DataFrame([{
        "temperature": t,
        "humidity": humidity,
        "promotion": promotion,
        "footfall": footfall,
        "avg_price": avg_price
    }]))[0] for t in temps]

    st.line_chart(pd.DataFrame({"Temperature": temps, "Revenue": preds}).set_index("Temperature"))
