import requests

class CachesClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def create_cache(self, payload):
        response = requests.post(f"{self.base_url}/caches", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()

    def delete_cache(self, cache_id):
        response = requests.delete(f"{self.base_url}/caches/{cache_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def fetch_cache_details(self, cache_id):
        response = requests.get(f"{self.base_url}/caches/{cache_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def list_caches(self):
        response = requests.get(f"{self.base_url}/caches", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_cache(self, cache_id, payload):
        response = requests.put(f"{self.base_url}/caches/{cache_id}", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()