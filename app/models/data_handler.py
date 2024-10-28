class DataHandler:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def get_users(self):
        return self.users

    def get_user(self, user_id):
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    def update_user(self, user_id, name, last_name):
        user = self.get_user(user_id)
        if user:
            user.name = name
            user.last_name = last_name
            return user
        return None

    def delete_user(self, user_id):
        user = self.get_user(user_id)
        if user:
            self.users.remove(user)
            return True
        return False

    def authenticate(self, username, password):
        for user in self.users:
            if user.name == username and user.check_password(password):
                return user
        return None


data_handler = DataHandler()
