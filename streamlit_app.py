import pandas as pd
import streamlit as st
import plotly.express as px
import joblib

st.set_page_config(page_title="Churn Predictor Dashboard", layout="wide")

st.title("📉 Customer Churn Prediction Dashboard")

df = pd.read_csv("data/sample_clients.csv")
model = joblib.load("model/churn_model.pkl")

df["churn_risk"] = model.predict_proba(df.drop(columns=["customer_id", "churn"]))[:,1]
df["risk_level"] = pd.cut(df["churn_risk"], bins=[0,0.3,0.7,1], labels=["Low", "Medium", "High"])

st.dataframe(df[["customer_id", "churn_risk", "risk_level"]].sort_values(by="churn_risk", ascending=False))

fig = px.histogram(df, x="churn_risk", nbins=20, title="Distribution of Churn Risk")
st.plotly_chart(fig)