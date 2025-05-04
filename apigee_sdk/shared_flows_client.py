import requests

class SharedFlowsClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def create_shared_flow(self, payload):
        response = requests.post(f"{self.base_url}/shared-flows", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()

    def delete_shared_flow(self, shared_flow_id):
        response = requests.delete(f"{self.base_url}/shared-flows/{shared_flow_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def fetch_shared_flow_details(self, shared_flow_id):
        response = requests.get(f"{self.base_url}/shared-flows/{shared_flow_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def list_shared_flows(self):
        response = requests.get(f"{self.base_url}/shared-flows", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_shared_flow(self, shared_flow_id, payload):
        response = requests.put(f"{self.base_url}/shared-flows/{shared_flow_id}", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()