# portal/login_test/hash_password.py

from models.mongodb.db import db
import hashlib
import secrets

# returns a random 16-byte string to be used as salt
def generate_salt():
    return secrets.token_hex(16)

# Combine password and salt, then hash using SHA-256
def hash_password(password, salt):
    return hashlib.sha256((password + salt).encode('utf-8')).hexdigest()

def register_portal_user(username, password):
    # Check if the user already exists in the database
    existing_user = db['portal_users'].find_one({'username': username})
    if existing_user:
        return
    # If the user does not exist, proceed with registration
    salt = generate_salt()
    hashed_password = hash_password(password, salt)
    db.portal_users.insert_one({
        'username': username,
        'hashed_password': hashed_password,
        'salt': salt
    })