import streamlit as st
import pandas as pd
import plotly.express as px
from db import get_user_predictions

# Safe session key init
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'email' not in st.session_state:
    st.session_state.email = ""

# Guard login
if not st.session_state.logged_in:
    st.warning("🔐 Please log in from the Login page.")
    st.stop()

# Sidebar
st.sidebar.markdown(f"👤 Logged in as: `{st.session_state.email}`")
if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.session_state.email = ""
    st.success("✅ You have been logged out.")
    st.stop()

# Page content
st.title("📚 Your Prediction History")

rows = get_user_predictions(st.session_state.email)
if rows:
    df = pd.DataFrame(rows, columns=["Recency", "Frequency", "Predicted CLV (₹)", "Timestamp"])
    st.dataframe(df, use_container_width=True)
    fig = px.line(df, y="Predicted CLV (₹)", title="CLV Trend", markers=True)
    st.plotly_chart(fig)
else:
    st.info("You haven't made any predictions yet.")
