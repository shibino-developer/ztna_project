from flask import Flask, render_template, request, jsonify, current_app
from ztna.auth import authenticate_user, generate_token, verify_token
from ztna.access_control import authorize_access
from functools import wraps
import jwt
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNzIxMjE2MDczfQ.JEi-OvKL-acSD4gbogPbUfRStKRAnz3yKK29SW5T4bI'

# Routes

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if authenticate_user(username, password):
        token = generate_token(username)
        return jsonify({'token': token.decode('UTF-8')})  # Decode byte string to UTF-8
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/access', methods=['POST'])
def access():
    data = request.json
    token = data.get('token')
    resource = data.get('resource')
    if authorize_access(token, resource):
        return jsonify({'message': 'Access granted'})
    return jsonify({'error': 'Access denied'}), 403

# Decorator function to enforce token authentication
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization', '').split()[1]  # Extract token from header
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            # Decode the token using the secret key
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 401

        return f(*args, **kwargs)

    return decorated

# Example protected route that requires token authentication
@app.route('/api/user/profile', methods=['GET'])
@token_required
def get_user_profile():
    # Example logic to retrieve and return user profile information
    user_profile = {
        'username': 'example_user',
        'email': 'example@example.com',
        'role': 'admin'  # Example: Include role-based data as needed
    }
    return jsonify(user_profile)

if __name__ == '__main__':
    app.run(debug=True)