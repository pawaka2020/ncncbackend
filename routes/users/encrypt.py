# # routes/users/encrypt.py

from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# # Generate encryption key based on user_id
def generate_encryption_key(user_id):
    # Convert user_id to bytes
    user_id_bytes = str(user_id).encode('utf-8')
    
    # Use SHA-256 hash function to generate a 256-bit key
    encryption_key = sha256(user_id_bytes).digest()
    
    return encryption_key

def encrypt_image(image_base64, user_id):
    # Decode base64-encoded image
    image_bytes = base64.b64decode(image_base64)
    
    # Generate encryption key based on user_id
    encryption_key = generate_encryption_key(user_id)
    
    # Initialize AES cipher in CBC mode with random IV
    cipher = AES.new(encryption_key, AES.MODE_CBC)
    
    # Pad the image bytes to match AES block size
    padded_image_bytes = pad(image_bytes, AES.block_size)
    
    # Encrypt the padded image bytes
    encrypted_image_bytes = cipher.encrypt(padded_image_bytes)
    
    # Combine IV and encrypted image bytes
    iv_and_encrypted_image = cipher.iv + encrypted_image_bytes
    
    # Encode the IV and encrypted image bytes in base64
    encrypted_image_base64 = base64.b64encode(iv_and_encrypted_image).decode('utf-8')
    
    return encrypted_image_base64