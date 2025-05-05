from typing import Dict, Any
import requests

class KeystoresClient:
    """
    Client to manage keystores in Apigee Edge.

    This client provides methods to create, update, delete, and fetch details of keystores.

    Attributes:
        base_url (str): The base URL for the Apigee API.
        headers (dict): The headers used for API requests, including the authorization token.
    """

    def __init__(self, base_url: str, token: str) -> None:
        """
        Initializes the KeystoresClient with the base URL and authorization token.

        Args:
            base_url (str): The base URL for the Apigee API.
            token (str): The authorization token for accessing the API.
        """
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def create_keystore(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new keystore in the Apigee environment.

        Args:
            payload (dict): The payload containing keystore details.

        Returns:
            dict: The response from the API containing details of the created keystore.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.post(f"{self.base_url}/keystores", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()

    def delete_keystore(self, keystore_id: str) -> Dict[str, Any]:
        """
        Deletes a keystore by its ID.

        Args:
            keystore_id (str): The ID of the keystore to delete.

        Returns:
            dict: The response from the API confirming the deletion.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.delete(f"{self.base_url}/keystores/{keystore_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def fetch_keystore_details(self, keystore_id: str) -> Dict[str, Any]:
        """
        Fetches details of a specific keystore by its ID.

        Args:
            keystore_id (str): The ID of the keystore to fetch details for.

        Returns:
            dict: The response from the API containing keystore details.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.get(f"{self.base_url}/keystores/{keystore_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def list_keystores(self) -> Dict[str, Any]:
        """
        Lists all keystores in the Apigee environment.

        Returns:
            dict: The response from the API containing a list of keystores.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.get(f"{self.base_url}/keystores", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_keystore(self, keystore_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates an existing keystore by its ID.

        Args:
            keystore_id (str): The ID of the keystore to update.
            payload (dict): The payload containing updated keystore details.

        Returns:
            dict: The response from the API containing details of the updated keystore.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.put(f"{self.base_url}/keystores/{keystore_id}", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()