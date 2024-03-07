# models/user.py

# postgreSQL commands:
# delete all entries : 
#DELETE FROM users;
# \d users

from datetime import datetime
from .db import db

# Define the User model
class User(db.Model):
    __tablename__ = 'users'

    # Proprietary fields
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(255))
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    birthday = db.Column(db.Date)
    phone_number = db.Column(db.String(20))
    address = db.Column(db.Text)
    profile_image = db.Column(db.String(255))
    coins = db.Column(db.Integer)
    guest = db.Column(db.Boolean)
    is_logged_in = db.Column(db.Boolean)
    new_user = db.Column(db.Boolean)
    set_default_address = db.Column(db.Boolean)

    # Relationships with classes below it.
    #cartitem = db.Relationship("CartItem", backref = 'user', lazy=True)

def find_registered_user(phone_number):
    # Query the 'users' table to find a matching entry
    user = User.query.filter_by(phone_number=phone_number, is_logged_in=False).first()

    if user:
        # Return the user object or user data
        return user
    else:
        # Return None if no matching user was found
        return None

def find_user_by_email(email):
    # Query the 'users' table to find a matching entry
    user = User.query.filter_by(email=email, is_logged_in=False).first()

    if user:
        # Return the user object or user data
        return user
    else:
        # Return None if no matching user was found
        return None

# takes a 'user' object, finds the matching 'entry' in the 'users' table by its 'id', 
# then flips the entry's 'is_logged_in' value to its opposite end ie if originally true then false, if false then true
def flip_user_log_status(user):
    if user is None:
        return False

    # Retrieve the user entry from the database using the provided user's id
    user_entry = User.query.filter_by(id=user.id).first()

    # If the user entry is found, flip the value of 'is_logged_in'
    if user_entry:
        user_entry.is_logged_in = not user_entry.is_logged_in
        # Commit the changes to the database
        db.session.commit()
        return True
    else:
        return False

# write a new entry in 'users' table
def create_new_user(user_id, email):
    # Create a new User object with the provided user_id and phone_number
    # Assign starting values for the other fields of this User object
    new_user = User(
        user_id = user_id, 
        name = 'User',
        email = email,
        birthday = datetime(1900, 1, 1), # change this to DateTime(1900, 1, 1)
        phone_number= '',
        address = '',
        profile_image = '',
        coins = 0,
        guest = False,
        is_logged_in = True,
        new_user = True,
        set_default_address = False,
    )

    # Add the new user object to the session and commit changes to the database
    db.session.add(new_user)
    db.session.commit()

    print("New user created successfully")