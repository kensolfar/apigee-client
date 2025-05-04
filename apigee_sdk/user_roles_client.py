import requests

class UserRolesClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def create_user_role(self, payload):
        response = requests.post(f"{self.base_url}/user-roles", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()

    def delete_user_role(self, role_id):
        response = requests.delete(f"{self.base_url}/user-roles/{role_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def fetch_user_role_details(self, role_id):
        response = requests.get(f"{self.base_url}/user-roles/{role_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def list_user_roles(self):
        response = requests.get(f"{self.base_url}/user-roles", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_user_role(self, role_id, payload):
        response = requests.put(f"{self.base_url}/user-roles/{role_id}", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()