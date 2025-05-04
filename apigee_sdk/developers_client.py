import requests

class DevelopersClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def create_developer(self, payload):
        response = requests.post(f"{self.base_url}/developers", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()

    def delete_developer(self, developer_id):
        response = requests.delete(f"{self.base_url}/developers/{developer_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def fetch_developer_details(self, developer_id):
        response = requests.get(f"{self.base_url}/developers/{developer_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def list_developers(self):
        response = requests.get(f"{self.base_url}/developers", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_developer(self, developer_id, payload):
        response = requests.put(f"{self.base_url}/developers/{developer_id}", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()