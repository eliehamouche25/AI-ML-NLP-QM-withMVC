class UserController:
    def __init__(self):
        self.users = {
            'elie': {'password': 'pass123', 'role': 'admin'},
            'admin': {'password': 'adminpass', 'role': 'admin'},
            'user': {'password': 'user123', 'role': 'guest'}
        }

    def authenticate_user(self, username, password):
        user = self.users.get(username)
        if user and user['password'] == password:
            return {'username': username, 'role': user['role']}
        return None

    def verify_user(self, username, password):
        stored_password = self.users.get(username, {}).get('password')
        return stored_password == password