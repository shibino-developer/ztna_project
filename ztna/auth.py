# ztna/auth.py
from datetime import datetime, timedelta
import jwt

# Example authentication function (replace with actual implementation)
def authenticate_user(username, password):
    # Replace with actual logic to verify user credentials
    if username == 'user' and password == 'password':
        return True
    else:
        return False

# Example function to generate JWT token
def generate_token(username):
    # Replace with your actual secret key configuration
    secret_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNzIxMjE2MDczfQ.JEi-OvKL-acSD4gbogPbUfRStKRAnz3yKK29SW5T4bI'
    
    # Define payload (data to be encoded in the token)
    payload = {
        'username': username,
        'exp': datetime.utcnow() + timedelta(hours=1)  # Token expiration time (e.g., 1 hour)
    }
    
    # Generate JWT token
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

# Example function to verify JWT token
def verify_token(token):
    try:
        payload = jwt.decode(token, 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNzIxMjE2MDczfQ.JEi-OvKL-acSD4gbogPbUfRStKRAnz3yKK29SW5T4bI', algorithms=['HS256'])
        return payload  # Return decoded payload
    except jwt.ExpiredSignatureError:
        return 'expired'  # Token has expired
    except jwt.InvalidTokenError:
        return 'invalid'  # Invalid token
