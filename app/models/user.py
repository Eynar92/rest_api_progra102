import uuid
import bcrypt

class User:
    def __init__(self, name, last_name, password):
        self.id = str(uuid.uuid4())
        self.name = name
        self.last_name = last_name
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password)