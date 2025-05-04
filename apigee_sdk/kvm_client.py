import requests

class KVMClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def create_kvm(self, payload):
        response = requests.post(f"{self.base_url}/kvms", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()

    def delete_kvm(self, kvm_id):
        response = requests.delete(f"{self.base_url}/kvms/{kvm_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def fetch_kvm_details(self, kvm_id):
        response = requests.get(f"{self.base_url}/kvms/{kvm_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def list_kvms(self):
        response = requests.get(f"{self.base_url}/kvms", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_kvm(self, kvm_id, payload):
        response = requests.put(f"{self.base_url}/kvms/{kvm_id}", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()