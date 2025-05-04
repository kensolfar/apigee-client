import requests

class DeveloperAppClient:
    """Client to manage developer apps in Apigee Edge."""
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def _handle_request_errors(self, response):
        """Handles common HTTP request errors."""
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            if response.status_code >= 400 and response.status_code < 500:
                error_message = response.json().get("message", "Unknown error")
                raise Exception(f"Error {response.status_code}: {error_message}")
            raise Exception(f"HTTP error occurred: {http_err}")
        except Exception as err:
            raise Exception(f"Failed to process the request: {err}")

    def add_api_key(self, app_id, payload):
        url = f"{self.base_url}/apps/{app_id}/api-keys"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.post(url, headers=headers, json=payload)
        self._handle_request_errors(response)
        return response.json()

    def approve_api_key(self, app_id, api_key_id):
        url = f"{self.base_url}/apps/{app_id}/api-keys/{api_key_id}/approve"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.post(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def create_app(self, payload):
        url = f"{self.base_url}/apps"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.post(url, headers=headers, json=payload)
        self._handle_request_errors(response)
        return response.json()

    def delete_app(self, app_id):
        url = f"{self.base_url}/apps/{app_id}"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.delete(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def fetch_app_details(self, app_id):
        url = f"{self.base_url}/apps/{app_id}"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def list_apps(self):
        url = f"{self.base_url}/apps"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def revoke_api_key(self, app_id, api_key_id):
        url = f"{self.base_url}/apps/{app_id}/api-keys/{api_key_id}/revoke"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.post(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def update_app(self, app_id, payload):
        url = f"{self.base_url}/apps/{app_id}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.put(url, headers=headers, json=payload)
        self._handle_request_errors(response)
        return response.json()