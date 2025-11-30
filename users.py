import json
import os
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

USERS_FILE = "users_data.json"

def load_users():
    """Load users from JSON file"""
    if not os.path.exists(USERS_FILE):
        # Create empty users file if it doesn't exist
        save_users({})
        return {}

    try:
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        # If file is corrupted, reset it
        print(f"⚠️ Warning: {USERS_FILE} was corrupted. Creating new file.")
        save_users({})
        return {}

def save_users(users):
    """Save users to JSON file"""
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def user_exists(email):
    """Check if user already exists"""
    users = load_users()
    return email.lower() in users

def register_user(email, password):
    """Register a new user with hashed password"""
    email = email.lower().strip()

    # Check if user already exists
    if user_exists(email):
        return False, "Email already registered"

    # Validate password length
    if len(password) < 6:
        return False, "Password must be at least 6 characters"

    # Load existing users
    users = load_users()

    # Create new user
    users[email] = {
        "email": email,
        "password_hash": generate_password_hash(password),
        "created_at": datetime.now().isoformat(),
    }

    # Save to file
    save_users(users)

    print(f"✅ New user registered: {email}")
    return True, "User registered successfully"

def verify_user(email, password):
    """Verify user credentials - returns True only if password matches"""
    email = email.lower().strip()
    users = load_users()

    # Check if user exists
    user = users.get(email)
    if not user:
        return False, "No account found with this email"

    # Verify password
    if check_password_hash(user["password_hash"], password):
        print(f"✅ User logged in: {email}")
        return True, "Login successful"

    return False, "Incorrect password"

def get_user_info(email):
    """Get user information (without password hash)"""
    email = email.lower().strip()
    users = load_users()

    user = users.get(email)
    if not user:
        return None

    # Return user info without password hash
    return {
        "email": user["email"],
        "created_at": user.get("created_at", "Unknown")
    }