import requests

class UsersClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def create_user(self, payload):
        response = requests.post(f"{self.base_url}/users", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()

    def delete_user(self, user_id):
        response = requests.delete(f"{self.base_url}/users/{user_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def fetch_user_details(self, user_id):
        response = requests.get(f"{self.base_url}/users/{user_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def list_users(self):
        response = requests.get(f"{self.base_url}/users", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_user(self, user_id, payload):
        response = requests.put(f"{self.base_url}/users/{user_id}", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()