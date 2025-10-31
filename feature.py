users = {
    "login": "test_user",
    "password": "secret_password"
}

def auth(login, password):
    if users.get(login) == password:
        return True
    else:
        return False