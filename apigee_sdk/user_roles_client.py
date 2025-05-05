from typing import Dict, Any
import requests

class UserRolesClient:
    """
    Client to manage user roles in Apigee Edge.

    This client provides methods to create, update, delete, and fetch details of user roles.

    Attributes:
        base_url (str): The base URL for the Apigee API.
        headers (dict): The headers used for API requests, including the authorization token.
    """

    def __init__(self, base_url: str, token: str) -> None:
        """
        Initializes the UserRolesClient with the base URL and authorization token.

        Args:
            base_url (str): The base URL for the Apigee API.
            token (str): The authorization token for accessing the API.
        """
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def create_user_role(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new user role in the Apigee environment.

        Args:
            payload (dict): The payload containing user role details.

        Returns:
            dict: The response from the API containing details of the created user role.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.post(f"{self.base_url}/user-roles", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()

    def delete_user_role(self, role_id: str) -> Dict[str, Any]:
        """
        Deletes a user role by its ID.

        Args:
            role_id (str): The ID of the user role to delete.

        Returns:
            dict: The response from the API confirming the deletion.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.delete(f"{self.base_url}/user-roles/{role_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def fetch_user_role_details(self, role_id: str) -> Dict[str, Any]:
        """
        Fetches details of a specific user role by its ID.

        Args:
            role_id (str): The ID of the user role to fetch details for.

        Returns:
            dict: The response from the API containing user role details.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.get(f"{self.base_url}/user-roles/{role_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def list_user_roles(self) -> Dict[str, Any]:
        """
        Lists all user roles in the Apigee environment.

        Returns:
            dict: The response from the API containing a list of user roles.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.get(f"{self.base_url}/user-roles", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_user_role(self, role_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates an existing user role by its ID.

        Args:
            role_id (str): The ID of the user role to update.
            payload (dict): The payload containing updated user role details.

        Returns:
            dict: The response from the API containing details of the updated user role.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.put(f"{self.base_url}/user-roles/{role_id}", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()