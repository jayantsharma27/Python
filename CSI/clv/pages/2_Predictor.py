import streamlit as st
import numpy as np
import joblib
from db import insert_prediction

# Safe session keys
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'email' not in st.session_state:
    st.session_state.email = ""

# Guard login
if not st.session_state.logged_in:
    st.warning("🔐 Please log in from the Login page.")
    st.stop()

# Sidebar Info
st.sidebar.markdown(f"👤 Logged in as: `{st.session_state.email}`")

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.email = ""
    st.success("✅ You have been logged out.")
    st.stop()

# Page content
st.title("📊 Predict Customer Lifetime Value")
st.markdown("Estimate the Customer Lifetime Value (CLV) based on customer behavior.")

model = joblib.load("clv_model.pkl")

recency = st.number_input("Recency (days since last purchase)", min_value=0, max_value=1000, value=100)
frequency = st.number_input("Frequency (number of purchases)", min_value=1, max_value=100, value=5)

if st.button("Predict CLV"):
    input_data = np.array([[recency, frequency]])
    prediction = round(model.predict(input_data)[0], 2)
    insert_prediction(st.session_state.email, recency, frequency, prediction)
    st.success(f"💰 Predicted CLV: ₹ {prediction}")
