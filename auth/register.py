users = {}

def register(username, password_hash):
    if username in users:
        return False
    users[username] = password_hash
    return True
