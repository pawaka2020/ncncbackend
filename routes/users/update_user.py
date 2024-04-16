# routes/users/update_user.py

from flask import Blueprint, request, jsonify
from models.mongodb.user import User
from blueprints import users_bp
from models.mongodb.db import db
import os
import base64

# Update user in 'users' collection
@users_bp.route('/api/update_user', methods=['POST'])
def update_user():
    # Obtain data from JSON sent to this route
    json_data = request.get_json()

    # Find the user in the database
    user = db.users.find_one({'user_id': json_data.get('user_id')})

    # Extract image base64 data from JSON    
    store_image(json_data.get('image_base_64'), json_data.get('user_id'))

    if user:
        # Update user fields with new data from JSON
        user['name'] = json_data.get('name')
        user['email'] = json_data.get('email')
        user['birthday'] = json_data.get('birthday')
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

        #save_profile_image(user['user_id'], user['profile_image'])

        return jsonify({'message': 'User updated successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404

def store_image(image_base64, user_id):
    # Decode base64-encoded image
    image_bytes = base64.b64decode(image_base64)
    
    # Define directory path
    directory = os.path.join('D:', 'python', 'ncncbackend', 'static', 'images', 'users', str(user_id))
    print("directory created as ", directory)

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
            print("file path defined as ", file_path)

            # Write image bytes to file
            with open(file_path, 'wb') as f:
                f.write(image_bytes)
            print('Profile image saved successfully')
        except Exception as e:
            print(f'Error occurred while saving profile image: {str(e)}')
    else:
        print('Empty image bytes. Profile image saving failed')
    
    image_bytes = base64.b64decode(image_base64)
    directory = os.path.join('D:', 'python', 'ncncbackend', 'static', 'images', 'users', str(user_id))
    print("directory = ", directory)

    # if (image_bytes):
    #     # Create directory if it doesn't exist
    #     if not os.path.exists(directory):
    #         os.makedirs(directory)
    #         print("directory created")
    #     else:
    #         print("directory not created")

    #     # Define file path for profile image
    #     file_path = os.path.join(directory, 'profile_image.jpg')

    #     # Write image bytes to file
    #     with open(file_path, 'wb') as f:
    #         f.write(image_bytes)
    #     print('Profile image saved successfully')
    # else:
    #     print('Profile image saving failed')

# saves profile image to the backend
# grabs only the .jpg file name from 'profile_image'
# save location: "D:\python\ncncbackend\static\images\users\user_id\profile_image"
# def save_profile_image(user_id, profile_image):
    # # Grab the file name and extension from profile_image
    # _, file_name = os.path.split(profile_image)
    # file_name, ext = os.path.splitext(file_name)

    # # Define the directory path to save the profile image
    # directory = os.path.join('D:', 'python', 'ncncbackend', 'static', 'images', 'users', str(user_id))
    # print("directory = ", directory)

    # # Create the directory if it doesn't exist
    # if not os.path.exists(directory):
    #     os.makedirs(directory)

    # # Define the file path for the profile image
    # file_path = os.path.join(directory, f"profile_image{ext}")

    # # Write the profile image data to the file
    # with open(file_path, 'wb') as f:
    #     f.write(profile_image.encode())  # Assuming profile_image is a base64 encoded string

    # print("Profile image saved successfully at:", file_path)