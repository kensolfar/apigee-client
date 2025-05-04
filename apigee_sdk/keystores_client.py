import requests

class KeystoresClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def create_keystore(self, payload):
        response = requests.post(f"{self.base_url}/keystores", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()

    def delete_keystore(self, keystore_id):
        response = requests.delete(f"{self.base_url}/keystores/{keystore_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def fetch_keystore_details(self, keystore_id):
        response = requests.get(f"{self.base_url}/keystores/{keystore_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def list_keystores(self):
        response = requests.get(f"{self.base_url}/keystores", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_keystore(self, keystore_id, payload):
        response = requests.put(f"{self.base_url}/keystores/{keystore_id}", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()