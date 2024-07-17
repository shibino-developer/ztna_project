# ztna/access_control.py
import jwt
from config import SECRET_KEY
from ztna.auth import verify_token

resources = {
    'admin': ['resource1', 'resource2'],
    'user': ['resource1']
}

def authorize_access(token, resource):
    result = verify_token(token)
    if isinstance(result, dict) and result.get('username'):
        # Here you can implement access control logic based on the user's role or permissions
        # Example: Check if the user has access to the requested resource
        if resource == 'protected_resource':
            return True
    return False
