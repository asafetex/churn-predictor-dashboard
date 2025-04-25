# 📉 Churn Predictor Dashboard – Customer Health Scoring with ML

This project demonstrates a practical machine learning application for predicting customer churn based on behavioral data. It uses logistic regression to calculate churn risk and displays an interactive dashboard via Streamlit for Customer Success teams.

## 🎯 Objective
Anticipate which customers are at high risk of churn based on their interaction history, support tickets, purchase recency, and more. Enable CS teams to proactively retain users.

## 🧠 Features
- Predicts churn likelihood using logistic regression
- Displays customer health scores in a visual dashboard
- Allows filtering and exporting of high-risk accounts
- Built for fast iteration and real-time CS feedback loops

## 🛠 Tech Stack
- Python (pandas, scikit-learn, Streamlit)
- CSV as data source (can be expanded to DB)
- Visualizations with Plotly

## 🗂️ Structure
```
churn-predictor-dashboard/
├── churn_model.ipynb          # Model training & evaluation
├── streamlit_app.py           # Frontend dashboard
├── data/sample_clients.csv    # Example customer dataset
├── requirements.txt
└── README.md
```

## ✅ Results
- Enables segmentation of at-risk users
- Assists CS reps with data-backed outreach
- Scalable approach to customer retention