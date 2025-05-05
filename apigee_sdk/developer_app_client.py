from typing import Dict, Any
import requests

class DeveloperAppClient:
    """
    Client to manage developer apps in Apigee Edge.

    This client provides methods to create, update, delete, and manage API keys for developer apps.

    Attributes:
        base_url (str): The base URL for the Apigee API.
        token (str): The authorization token for accessing the API.
    """

    def __init__(self, base_url: str, token: str) -> None:
        """
        Initializes the DeveloperAppClient with the base URL and authorization token.

        Args:
            base_url (str): The base URL for the Apigee API.
            token (str): The authorization token for accessing the API.
        """
        self.base_url = base_url
        self.token = token

    def _handle_request_errors(self, response: requests.Response) -> None:
        """
        Handles common HTTP request errors.

        Args:
            response (requests.Response): The HTTP response object.

        Raises:
            Exception: If an HTTP error or other error occurs.
        """
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as http_err:
            if response.status_code >= 400 and response.status_code < 500:
                error_message = response.json().get("message", "Unknown error")
                raise Exception(f"Error {response.status_code}: {error_message}")
            raise Exception(f"HTTP error occurred: {http_err}")
        except Exception as err:
            raise Exception(f"Failed to process the request: {err}")

    def add_api_key(self, app_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Adds an API key to a developer app.

        Args:
            app_id (str): The ID of the developer app.
            payload (dict): The payload containing API key details.

        Returns:
            dict: The response from the API containing the added API key details.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/apps/{app_id}/api-keys"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.post(url, headers=headers, json=payload)
        self._handle_request_errors(response)
        return response.json()

    def approve_api_key(self, app_id: str, api_key_id: str) -> Dict[str, Any]:
        """
        Approves an API key for a developer app.

        Args:
            app_id (str): The ID of the developer app.
            api_key_id (str): The ID of the API key to approve.

        Returns:
            dict: The response from the API confirming the approval.

        Raises:
            requests.exceptions.HTTPError: If the API request fails.
        """
        url = f"{self.base_url}/apps/{app_id}/api-keys/{api_key_id}/approve"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.post(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def create_app(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new developer app.

        Args:
            payload (dict): The payload containing app details.

        Returns:
            dict: The response from the API containing the created app details.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/apps"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.post(url, headers=headers, json=payload)
        self._handle_request_errors(response)
        return response.json()

    def delete_app(self, app_id: str) -> Dict[str, Any]:
        """
        Deletes a developer app by its ID.

        Args:
            app_id (str): The ID of the developer app to delete.

        Returns:
            dict: The response from the API confirming the deletion.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/apps/{app_id}"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.delete(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def fetch_app_details(self, app_id: str) -> Dict[str, Any]:
        """
        Fetches details of a specific developer app by its ID.

        Args:
            app_id (str): The ID of the developer app.

        Returns:
            dict: The response from the API containing app details.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/apps/{app_id}"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def list_apps(self) -> Dict[str, Any]:
        """
        Lists all developer apps.

        Returns:
            dict: The response from the API containing a list of developer apps.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/apps"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def revoke_api_key(self, app_id: str, api_key_id: str) -> Dict[str, Any]:
        """
        Revokes an API key for a developer app.

        Args:
            app_id (str): The ID of the developer app.
            api_key_id (str): The ID of the API key to revoke.

        Returns:
            dict: The response from the API confirming the revocation.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/apps/{app_id}/api-keys/{api_key_id}/revoke"
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.post(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def update_app(self, app_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates an existing developer app by its ID.

        Args:
            app_id (str): The ID of the developer app to update.
            payload (dict): The payload containing updated app details.

        Returns:
            dict: The response from the API containing the updated app details.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/apps/{app_id}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.put(url, headers=headers, json=payload)
        self._handle_request_errors(response)
        return response.json()