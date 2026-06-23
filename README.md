# 🍦 Ice-Cream Revenue Predictor

A Streamlit-based Machine Learning application that predicts the expected daily revenue of an ice-cream shop based on weather conditions, customer footfall, pricing, promotions, and product preferences.

## 📌 Project Overview

The Ice-Cream Revenue Predictor helps shop owners estimate their daily revenue using a trained machine learning model. Users can enter various business and environmental factors, and the application generates a revenue prediction instantly.

The project demonstrates the practical application of machine learning in business forecasting and decision-making.

## 🚀 Features

- Predict daily ice-cream shop revenue
- User-friendly Streamlit interface
- Weather-based revenue estimation
- Promotion impact analysis
- Flavor selection support
- Cup vs Cone sales ratio consideration
- Toppings influence on revenue
- Interactive revenue visualization chart
- Real-time predictions

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib

## 📂 Project Structure

```
IceCreamRevenuePredictor/
│
├── app.py
├── models/
│   └── revenue_model.pkl
├── requirements.txt
├── README.md
└── dataset/
```

## 📊 Input Parameters

The application uses the following inputs:

| Parameter | Description |
|------------|-------------|
| Temperature | Current temperature (°C) |
| Humidity | Humidity percentage |
| Footfall | Estimated number of customers |
| Average Price | Average price per item |
| Promotion | Whether a promotion is running |
| Flavor | Ice-cream flavor selected |
| Cup vs Cone Ratio | Percentage of cup sales |
| Toppings | Availability of toppings |

## 🎯 Output

The model predicts:

- Expected Daily Revenue ($)

Additionally, the application displays:

- Temperature vs Revenue trend graph

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/IceCreamRevenuePredictor.git
cd IceCreamRevenuePredictor
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

## 📈 Machine Learning Model

The application loads a pre-trained machine learning model using Joblib:

```python
model = joblib.load("models/revenue_model.pkl")
```

The model predicts revenue based on:

- Temperature
- Humidity
- Promotion
- Footfall
- Average Price

Additional factors such as flavor, toppings, and cup/cone ratio are incorporated to enhance the prediction experience.

## 🎓 Learning Outcomes

This project demonstrates:

- Machine Learning Model Deployment
- Streamlit Web Application Development
- Data Visualization
- Business Revenue Forecasting
- User Interface Design

## 🔮 Future Enhancements

- Real-time weather API integration
- Advanced machine learning models
- Historical revenue analytics
- Multiple store support
- Sales report generation
- Database integration
- Mobile-responsive design

## 🤝 Contribution

Contributions, suggestions, and improvements are welcome.

## 📄 License

This project is developed for educational and learning purposes.