from auth.session import sessions

def logout(token):
    return sessions.pop(token, None) is not None
