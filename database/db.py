import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
def create_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

def save_prediction(user_id, area, bedrooms, age, predicted_price):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO predictions
        (user_id, area, bedrooms, age, predicted_price)
        VALUES (%s,%s,%s,%s,%s)
    """,
    (user_id, area, bedrooms, age, predicted_price)
    )

    conn.commit()

    cursor.close()
    conn.close()

def get_predictions(user_id):

    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM predictions WHERE user_id = %s """,(user_id,))

    rows = cursor.fetchall()

    cursor.close()
    conn.close()


    return rows
def create_users_table():
    conn = create_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            username VARCHAR(100),
            email VARCHAR(255) UNIQUE,
            password_hash TEXT
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
def register_user(username , email, password_hash):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users
        (username, email , password_hash)
        VALUES (%s , %s , %s)
    """, (username , email, password_hash))
    conn.commit()
    cursor.close()
    conn.close()
def email_exists(email):

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE email = %s",
        (email,)
    )
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row:
        return True
    return False
def get_user_by_email(email):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, username, email, password_hash
        FROM users
        WHERE email = %s
    """, (email,))

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user
def create_predictions_table():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions(
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            area INTEGER,
            bedrooms INTEGER,
            age INTEGER,
            predicted_price REAL
        );
    """)

    conn.commit()

    cursor.close()
    conn.close()
