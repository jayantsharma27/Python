import streamlit as st
from db import register_user, verify_user

# Safe session key init
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'email' not in st.session_state:
    st.session_state.email = ""

st.title("🔐 Login / Signup")

auth_choice = st.radio("Choose option:", ["Login", "Signup"])
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if auth_choice == "Signup":
    if st.button("Create Account"):
        if not email or not password:
            st.warning("Please fill in both fields.")
        elif "@" not in email or "." not in email:
            st.warning("Please enter a valid email address.")
        elif register_user(email, password):
            st.success("✅ Account created! Please log in.")
        else:
            st.error("⚠️ Email already exists.")
else:
    if st.button("Login"):
        if not email or not password:
            st.warning("Please fill in both fields.")
        elif verify_user(email, password):
            st.session_state.logged_in = True
            st.session_state.email = email
            st.success(f"✅ Logged in as {email}")
        else:
            st.error("❌ Invalid email or password.")
