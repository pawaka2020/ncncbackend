# models/user.py

from .db import db

# Define the User model
class User(db.Model):
    __tablename__ = 'users'
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

def find_registered_user(phone_number):
    # Query the 'users' table to find a matching entry
    user = User.query.filter_by(phone_number=phone_number, is_logged_in=False).first()

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


#   Find the user with the provided phone number
#   user = find_registered_user(phone_number)
#   If a matching user is found and not already logged in
#   if user:
#     create_token_from_existing_user(user)
#   else:
#     create_token_from_new_user(phone_number)