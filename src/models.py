from uuid import uuid4
from hashlib import sha256


class User:
    
    def __init__(self, id: str, username: str, password: str, first_name: str, last_name: str):
        self.id = id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name


    @classmethod
    def from_dict(cls, user_data: dict):
        return cls(
                id=user_data['id'],
                username=user_data['username'],
                password=user_data['password'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
            )
    
    @classmethod
    def create_user(cls, username: str, password: str, first_name: str, last_name: str):
        return cls(
                id=str(uuid4()),
                username=username,
                password=str(sha256(password.encode()).hexdigest()),
                first_name=first_name,
                last_name=last_name,
            )