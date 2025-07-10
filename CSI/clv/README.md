# 📦 Customer Lifetime Value (CLV) Prediction Web App

A modern web app built with **Streamlit** that predicts the **Customer Lifetime Value** using purchase history. Users can register, log in securely, track their predictions, and visualize trends — all with a clean, multi-page UI.

---

## 🚀 Features

✅ Predict Customer Lifetime Value using:
- Recency (days since last purchase)  
- Frequency (number of purchases)

✅ User Authentication (Login/Signup)  
✅ Personalized Prediction History  
✅ Interactive Charts using Plotly  
✅ Multi-page UI with sidebar navigation  
✅ Ready for PostgreSQL deployment  
✅ Persistent user data tracking  

---

## 🛠 Tech Stack

- **Frontend/UI:** Streamlit (multi-page)
- **ML Model:** Gradient Boosting Regressor (`scikit-learn`)
- **Database:** SQLite (local) or PostgreSQL (for deployment)
- **Login System:** Secure hashed passwords with `hashlib`
- **Visualizations:** Plotly, Pandas

---

## 📂 Folder Structure

clv/
├── app.py ← Main entry point (Home page)
├── clv_model.py ← Trains the CLV prediction model
├── clv_model.pkl ← Saved ML model
├── requirements.txt ← All Python dependencies
├── data/
│ └── online_retail_II.xlsx
├── db.py ← Database logic (users, history)
├── pages/
│ ├── login_signup.py ← User registration and login
│ ├── predictor.py ← Prediction input + model inference
│ └── history.py ← User prediction history + graph

## 🧪 How to Run Locally

1. Clone the repo and move to `clv/`:
   cd csi/clv

Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate  # On Windows

Install dependencies:
pip install -r requirements.txt

Train model (only once):
python clv_model.py

Run the app:
streamlit run app.py

🗃 Future Enhancements
Switch to PostgreSQL for production
Password reset via email
Enhanced chart analytics
Admin dashboard to view user data
Deployment via Render, Railway, or Streamlit Cloud

👨‍💻 Author
Jayant Sharma
💼 Python | Streamlit | ML | Web Dev
📜 License
This project is open-source and free to use under the MIT License.
