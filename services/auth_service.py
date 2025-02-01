from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Function to verify user credentials (you can modify this based on your DB)
def verify_user(username, password):
    if username == "admin" and password == "password":
        return User(id=1)
    return None
