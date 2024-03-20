# models/mongodb/user.py

from .db import db
from datetime import datetime

class User:
    # Constructor and fields definition
    def __init__(self, address="", birthday="1900-01-01", cart_items=[], orders=[], coins=0, email="", guest=False, is_logged_in=True, name="User", new_user=True, phone_number="", profile_image="", set_default_address=False, user_id=""):
        self.address = address
        self.birthday = datetime.strptime("1900-01-01", "%Y-%m-%d")
        self.cart_items = cart_items
        self.orders = orders
        self.coins = coins
        self.email = email
        self.guest = guest
        self.is_logged_in = is_logged_in
        self.name = name
        self.new_user = new_user
        self.phone_number = phone_number
        self.profile_image = profile_image
        self.set_default_address = set_default_address
        self.user_id = user_id

    # Creates new 'User' object with provided 'user_id' and 'email'
    # Then writes this new object in 'users' collection
    @staticmethod
    def create_new(user_id, email):
        db.users.insert_one({
            'address': '',
            'birthday': datetime.strptime("1900-01-01", "%Y-%m-%d"), 
            'cart_items': [],
            'orders': [],
            'coins': 0,
            'email': email,
            'guest': False,    
            'is_logged_in': True,
            'name': 'User',
            'new_user': True,
            'phone_number': '',
            'profile_image': '',
            'set_default_address': False,
            'user_id': user_id
        })

    # Finds 'User' object with matching 'email'
    # If object located returns the object, else returns None
    @staticmethod
    def query_by_email(email):
        user = db['users'].find_one({'email': email})
        return user
        # if (user):
        #     return user
        # return None
    
    # Finds 'User' object with matching 'id'
    # If object located returns the object, else returns None
    # @staticmethod
    # def query_by_id(user_id):
    #     user = db['users'].find_one({'user_id': user_id})
    #     if (user):
    #         return user
    #     return None
    
    # @staticmethod
    # def query_by_id(user_id):
    #     user_data = db.users.find_one({'user_id': user_id})
    #     if user_data:
    #         return User(**user_data)  # Create User instance from dictionary
    #     else:
    #         return None

    # Finds 'User' object with matching'id', 
    # Flips object's 'is_logged_in' value to its opposite end ie if originally true then false, if false then true
    @staticmethod
    def flip_log_status(id):
        user = db['users'].find_one({'id': id})
        if user:
            new_log_status = not user['is_logged_in']
            db['users'].update_one({'id': id}, {'$set': {'is_logged_in': new_log_status}})











    # Method to save user data to the database (implementation may vary based on the database used)
    #db['countries'].
    def save(self):
        # Assuming db.users is the collection/table to store user data
        db.user.insert_one({
            'address': self.address,
            'birthday': self.birthday.strftime("%Y-%m-%d"),
            'cart_items': self.cart_items,
            'orders': self.orders,
            'coins': self.coins,
            'email': self.email,
            'guest': self.guest,
            'is_logged_in': self.is_logged_in,
            'name': self.name,
            'new_user': self.new_user,
            'phone_number': self.phone_number,
            'profile_image': self.profile_image,
            'set_default_address': self.set_default_address,
            'user_id': self.user_id
        })

    