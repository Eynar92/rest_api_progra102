import uuid

class User:
    def __init__(self, name, last_name):
        self.id = str(uuid.uuid4())
        self.name = name
        self.last_name = last_name
