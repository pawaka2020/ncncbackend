import random
import string
import base64
import hashlib
import json

def generate_auth_token(user_id, phone_number, guest=False, new_user=False):
    # Define the range of characters to be used for the token
    characters = string.ascii_letters + string.digits

    # Generate a token consisting of random characters
    token_length = 32
    random_token = ''.join(random.choice(characters) for _ in range(token_length))

    # Define the payload dictionary
    payload = {
        "userId": user_id,
        "phoneNumber": phone_number,
        "guest": guest,
        "newUser": new_user
    }

    # Serialize the payload to JSON
    payload_json = json.dumps(payload)

    # Attach the token to a secret key
    secret_key = 'blahblahblah'
    combined_string = random_token + secret_key + payload_json

    # Hash and encode
    hashed_token = hashlib.sha256(combined_string.encode()).hexdigest()
    auth_token = base64.urlsafe_b64encode(hashed_token.encode()).decode()

    return auth_token