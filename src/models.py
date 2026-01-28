from uuid import uuid4
from hashlib import sha256


class User:
    
    def __init__(self, username: str, password: str, first_name: str, last_name: str, id: str | None = None):
        self.username = username
        self.password = str(sha256(password.encode()).hexdigest())
        self.first_name = first_name
        self.last_name = last_name

        if id:
            self.id = id
        else:
            self.id = str(uuid4())

    @classmethod
    def from_dict(cls, user_data: dict):
        return cls(
               username=user_data['username'],
               password=user_data['password'],
               first_name=user_data['first_name'],
               last_name=user_data['last_name'],
               id=user_data['id'],
           )