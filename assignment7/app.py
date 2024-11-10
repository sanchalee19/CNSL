from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt

app = Flask(__name__)

# Simulating a database (replace with real DB for production)
users_db = {
    "chetan": {
        "username": "chetan",
        "password_hash": generate_password_hash("chetan")  # Example password hash
    }
}

# Home route for login page
@app.route('/')
def home():
    return render_template('index.html')

# Login route
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Check if user exists in the simulated DB
    user = users_db.get(username)
    if user and check_password_hash(user['password_hash'], password):
        return f"Welcome {username}!"
    else:
        return "Invalid username or password", 401

if __name__ == "__main__":
    app.run(debug=True)
