import json
import os
from werkzeug.security import generate_password_hash, check_password_hash

USERS_FILE = "users_data.json"

def load_users():
    """Load users from JSON file"""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    """Save users to JSON file"""
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

def user_exists(email):
    """Check if user already exists"""
    users = load_users()
    return email.lower() in users

def register_user(email, password):
    """Register a new user with hashed password"""
    if user_exists(email):
        return False, "Email already registered"
    
    if len(password) < 6:
        return False, "Password must be at least 6 characters"
    
    users = load_users()
    users[email.lower()] = {
        "password_hash": generate_password_hash(password),
        "email": email
    }
    save_users(users)
    return True, "User registered successfully"

def verify_user(email, password):
    """Verify user credentials - returns True only if exact password matches"""
    users = load_users()
    user = users.get(email.lower())
    
    if not user:
        return False, "User not found"
    
    if check_password_hash(user["password_hash"], password):
        return True, "Login successful"
    
    return False, "Incorrect password"
