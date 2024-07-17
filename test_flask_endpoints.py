import requests
import json

# Define the base URL of your Flask application
base_url = 'http://localhost:5000'

# Function to test the login endpoint
def test_login():
    url = f"{base_url}/login"
    headers = {'Content-Type': 'application/json'}
    data = {
        'username': 'user',
        'password': 'password'
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Function to test the authenticated profile endpoint
def test_profile(token):
    url = f"{base_url}/api/user/profile"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)
    return response.json()

# Main function to execute tests
def main():
    # Test login and obtain the token
    login_response = test_login()
    if 'token' in login_response:
        token = login_response['token']
        print(f"Login successful! Token: {token}")

        # Test profile endpoint with the obtained token
        profile_response = test_profile(token)
        print("Profile response:", profile_response)
    else:
        print("Login failed:", login_response)

if __name__ == "__main__":
    main()
