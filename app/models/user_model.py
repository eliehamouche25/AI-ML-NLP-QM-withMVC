
 
class UserModel:
    def __init__(self, username, email, password_hash, note='', role='guest'):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.note = note
        self.role = role