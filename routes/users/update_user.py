# routes/users/update_user.py

from flask import Blueprint, request, jsonify
from models.mongodb.user import User
from blueprints import users_bp
from models.mongodb.db import db
import os
import base64
from datetime import datetime

# fix this. store image should come after user verification
# Update user in 'users' collection
@users_bp.route('/api/update_user', methods=['POST'])
def update_user():
    # Obtain data from JSON sent to this route
    json_data = request.get_json()

    # Find the user in the database
    user = db.users.find_one({'user_id': json_data.get('user_id')})

    if user:
        # Update user fields with new data from JSON
        user['name'] = json_data.get('name')
        user['email'] = json_data.get('email')
        user['birthday'] = datetime.strptime(json_data.get('birthday').split('T')[0], "%Y-%m-%d")
        user['phone_number'] = json_data.get('phone_number')
        user['address'] = json_data.get('address')
        user['profile_image'] = json_data.get('profile_image')
        user['coins'] = json_data.get('coins')
        user['guest'] = json_data.get('guest')
        user['is_logged_in'] = json_data.get('is_logged_in')
        user['new_user'] = json_data.get('new_user')
        user['set_default_address'] = json_data.get('set_default_address')

        # child objects
        user['cart_items'] = json_data.get('cart_items')

        # Save the updated user object back to the database
        db.users.update_one({'user_id': json_data.get('user_id')}, {'$set': user})

        # Extract image base64 data from JSON    
        store_image(json_data.get('image_base_64'), json_data.get('user_id'))

        return jsonify({'message': 'User updated successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

def store_image(image_base64, user_id):
    # Decode base64-encoded image
    image_bytes = base64.b64decode(image_base64)
    
    # Define directory path
    directory = os.path.join('static', 'images', 'users', str(user_id))
    print("directory created as", directory)

    # Check if image bytes are not empty
    if image_bytes:
        print("image bytes present")
        try:
            # Create directory if it doesn't exist
            if not os.path.exists(directory):
                os.makedirs(directory)
                print("Directory created")
            else:
                print("Directory already exists")

            # Define file path for profile image
            file_path = os.path.join(directory, 'profile_image.jpg')
            print("file path defined as", file_path)

            # Write image bytes to file
            with open(file_path, 'wb') as f:
                f.write(image_bytes)
            print('Profile image saved successfully')
        except Exception as e:
            print(f'Error occurred while saving profile image: {str(e)}')
    else:
        # If image bytes are empty, delete existing profile image if it exists
        file_path = os.path.join(directory, 'profile_image.jpg')
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print('Existing profile image deleted successfully')
            except Exception as e:
                print(f'Error occurred while deleting existing profile image: {str(e)}')
        else:
            print('No existing profile image found. Nothing to delete.')
            
    # Decode base64-encoded image
    image_bytes = base64.b64decode(image_base64)
    
    # Define directory path
    directory = os.path.join('static', 'images', 'users', str(user_id))
    print("directory created as", directory)

    # Check if image bytes are not empty
    if (image_bytes):
        print("image bytes present")
        try:
            # Create directory if it doesn't exist
            if not os.path.exists(directory):
                os.makedirs(directory)
                print("Directory created")
            else:
                print("Directory already exists")

            # Define file path for profile image
            file_path = os.path.join(directory, 'profile_image.jpg')
            print("file path defined as", file_path)

            # Write image bytes to file
            with open(file_path, 'wb') as f:
                f.write(image_bytes)
            print('Profile image saved successfully')
        except Exception as e:
            print(f'Error occurred while saving profile image: {str(e)}')
    else:
        print('Empty image bytes. Profile image not saved.')