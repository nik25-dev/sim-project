from auth.register import users
from auth.password import hash_password

def login(username, password):
    return users.get(username) == hash_password(password)
