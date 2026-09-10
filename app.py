import pickle
import pandas as pd
import psycopg2
import logging
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask import Flask, render_template, request, session
from database.db import (
    register_user,
    email_exists,
    create_connection,
    create_users_table,
    save_prediction,
    get_predictions,
    get_user_by_email,
    create_predictions_table
)

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

app = Flask(__name__)
app.secret_key = "my_super_secret_key"

create_predictions_table()
with open("models/house_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    if "user_id" not in session:
        return "Please login first"
    area = float(request.form["area"])
    bedrooms = int(request.form["bedrooms"])
    age = int(request.form["age"])

    if area <= 0:
        return "<h2>Area must be greater than zero.</h2>"

    if bedrooms <= 0:
        return "<h2>Bedrooms must be greater than zero.</h2>"

    if age < 0:
        return "<h2>Age cannot be negative.</h2>"

    house = pd.DataFrame({
        "Area": [area],
        "Bedrooms": [bedrooms],
        "Age": [age]
    })

    prediction = model.predict(house)
    try:
        save_prediction(
            session["user_id"],
            area,
            bedrooms,
            age,
            float(prediction[0])
        )
        logging.info(
            f"Prediction made: Area={area}, Bedrooms={bedrooms}, Age={age}, Price={prediction[0]}"
        )
    except Exception as e:
        logging.error(f"Database Error: {e}")

    return render_template(
    "result.html",
       area=area,
       bedrooms=bedrooms,
       age=age,
       prediction=f"{prediction[0]:,.2f}"
    )

@app.route("/history")
def history():

    if "user_id" not in session:
        return "Please login first"

    try:
        rows = get_predictions(session["user_id"])
        return render_template("history.html", rows=rows)

    except Exception as e:
        print("HISTORY ERROR:", e)
        return str(e)


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/register", methods=["POST"])
def register_user_route():
    create_users_table()
    username = request.form["username"]
    email = request.form["email"]
    if email_exists(email):
        return "Email already registered!"
    password = request.form["password"]
    password_hash = generate_password_hash(password)
    register_user(
        username,
        email,
        password_hash
    )
    return """
        <h2>Registration Successful!</h2>

        <a href="/login">Login</a>
    """

@app.route("/login" , methods = ["GET"])
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_user():

    email = request.form["email"]
    password = request.form["password"]

    user = get_user_by_email(email)

    if user is None:
        return "<h2>Email not found!</h2>"

    if check_password_hash(user[3], password):
        session["user_id"] = user[0]
        session["username"] = user[1]
        return f"<h2>Welcome {user[1]}!</h2>"

    return "<h2>Incorrect password!</h2>"


@app.route("/logout")
def logout():

    session.clear()

    return """
    <h2>You have been logged out</h2>
    <a href="/">Home</a>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
