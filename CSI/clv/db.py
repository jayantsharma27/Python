# db.py

import sqlite3
from datetime import datetime
import hashlib

def get_connection():
    return sqlite3.connect('clv_history.db')

def init_db():
    conn = get_connection()
    c = conn.cursor()
    
    # Table for predictions
    c.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            recency INTEGER,
            frequency INTEGER,
            clv REAL,
            timestamp TEXT
        )
    ''')

    # Table for users
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Hash passwords for safety
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Signup logic
def register_user(username, password):
    conn = get_connection()
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)', 
                  (username, hash_password(password)))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # username already exists
    finally:
        conn.close()

# Login logic
def verify_user(username, password):
    conn = get_connection()
    c = conn.cursor()
    c.execute('SELECT password_hash FROM users WHERE username = ?', (username,))
    result = c.fetchone()
    conn.close()
    return result and result[0] == hash_password(password)

# Save prediction
def insert_prediction(username, recency, frequency, clv):
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        INSERT INTO predictions (username, recency, frequency, clv, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (username, recency, frequency, clv, datetime.now().isoformat()))
    conn.commit()
    conn.close()

# Get user prediction history
def get_user_predictions(username):
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        SELECT recency, frequency, clv, timestamp
        FROM predictions
        WHERE username = ?
        ORDER BY timestamp DESC
    ''', (username,))
    rows = c.fetchall()
    conn.close()
    return rows
