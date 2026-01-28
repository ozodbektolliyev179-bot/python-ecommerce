import json


class DB:

    def __init__(self):
        self.file_name = 'db.json'
    
    def get_user_by_username(self, username: str) -> dict | None:
        with open(self.file_name) as jsonfile:
            data = json.loads(jsonfile.read())

            for user in data['users']:
                if user['username'] == username:
                    return user

    def create_user(self, id: str, username: str, password: str, first_name: str, last_name: str):
        with open(self.file_name) as jsonfile:
            data = json.loads(jsonfile.read())

            data['users'].append({
                "id": id,
                "username": username,
                "password": password,
                "first_name": first_name,
                "last_name": last_name,
            })

        with open(self.file_name, 'w') as jsonfile:
            jsonfile.write(json.dumps(data, indent=4))