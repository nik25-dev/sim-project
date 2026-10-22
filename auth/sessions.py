import secrets

sessions = {}

def create_session(username):
    token = secrets.token_hex(8)
    sessions[token] = username
    return token
