import json
from uuid import uuid4


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

    def get_product_list(self) -> list[dict]:
        with open(self.file_name) as jsonfile:
            data = json.loads(jsonfile.read())

            return data['products']
        
    def get_cart_by_user(self, id: str):
        with open(self.file_name) as jsonfile:
            data = json.loads(jsonfile.read())

            for cart in data['carts']:
                if cart['user_id'] == id:
                    return cart
            new_cart = {
                'user_id': id,
                'cart_id': str(uuid4())
            }
            data['carts'].append(new_cart)
        
        with open(self.file_name, 'w') as jsonfile:
            jsonfile.write(json.dumps(data, indent=4))

        return new_cart

    def add_cart_item(self, cart: dict, product: dict):
        with open(self.file_name) as jsonfile:
            data = json.loads(jsonfile.read())

            for cart_item in data['cart_items']:
                if cart_item['cart_id'] == cart['cart_id'] and cart_item['product_id'] == product['id']:
                    cart_item['quantity'] += 1
                    break
            else:
                data['cart_items'].append({
                    'cart_id': cart['cart_id'],
                    'product_id': product['id'],
                    'quantity': 1
                })

        with open(self.file_name, 'w') as jsonfile:
            jsonfile.write(json.dumps(data, indent=4))

    def get_cart_items_by_cart(self, cart: dict):
        with open(self.file_name) as jsonfile:
            data = json.loads(jsonfile.read())

            result = []
            for cart_item in data['cart_items']:
                if cart_item['cart_id'] == cart['cart_id']:
                    result.append(cart_item)
            return result
        