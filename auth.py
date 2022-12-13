import base64

def get_authorization_header(user, pat):
    basic = f'{user}:{pat}'    
    encoded_auth = basic.encode('ascii')
    auth_bytes = base64.b64encode(encoded_auth)
    base64_auth = auth_bytes.decode('ascii')
    
    return { 'Authorization': f'Basic {base64_auth}'}    