from typing import Dict, Any
import requests

class UsersClient:
    """
    Client to manage users in Apigee Edge.

    This client provides methods to create, update, delete, and fetch details of users.

    Attributes:
        base_url (str): The base URL for the Apigee API.
        headers (dict): The headers used for API requests, including the authorization token.
    """

    def __init__(self, base_url: str, token: str) -> None:
        """
        Initializes the UsersClient with the base URL and authorization token.

        Args:
            base_url (str): The base URL for the Apigee API.
            token (str): The authorization token for accessing the API.
        """
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def create_user(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new user in the Apigee environment.

        Args:
            payload (dict): The payload containing user details.

        Returns:
            dict: The response from the API containing details of the created user.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.post(f"{self.base_url}/users", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()

    def delete_user(self, user_id: str) -> Dict[str, Any]:
        """
        Deletes a user by their ID.

        Args:
            user_id (str): The ID of the user to delete.

        Returns:
            dict: The response from the API confirming the deletion.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.delete(f"{self.base_url}/users/{user_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def fetch_user_details(self, user_id: str) -> Dict[str, Any]:
        """
        Fetches details of a specific user by their ID.

        Args:
            user_id (str): The ID of the user to fetch details for.

        Returns:
            dict: The response from the API containing user details.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.get(f"{self.base_url}/users/{user_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def list_users(self) -> Dict[str, Any]:
        """
        Lists all users in the Apigee environment.

        Returns:
            dict: The response from the API containing a list of users.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.get(f"{self.base_url}/users", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_user(self, user_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates an existing user by their ID.

        Args:
            user_id (str): The ID of the user to update.
            payload (dict): The payload containing updated user details.

        Returns:
            dict: The response from the API containing details of the updated user.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.put(f"{self.base_url}/users/{user_id}", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()