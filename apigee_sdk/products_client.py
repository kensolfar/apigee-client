import requests

class ProductsClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def create_product(self, payload):
        response = requests.post(f"{self.base_url}/products", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()

    def delete_product(self, product_id):
        response = requests.delete(f"{self.base_url}/products/{product_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def fetch_product_details(self, product_id):
        response = requests.get(f"{self.base_url}/products/{product_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def list_products(self):
        response = requests.get(f"{self.base_url}/products", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_product(self, product_id, payload):
        response = requests.put(f"{self.base_url}/products/{product_id}", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()