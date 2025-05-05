from typing import Dict, Any
import requests

class SharedFlowsClient:
    """
    Client to manage shared flows in Apigee Edge.

    This client provides methods to create, update, delete, and fetch details of shared flows.

    Attributes:
        base_url (str): The base URL for the Apigee API.
        headers (dict): The headers used for API requests, including the authorization token.
    """

    def __init__(self, base_url: str, token: str) -> None:
        """
        Initializes the SharedFlowsClient with the base URL and authorization token.

        Args:
            base_url (str): The base URL for the Apigee API.
            token (str): The authorization token for accessing the API.
        """
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def create_shared_flow(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new shared flow in the Apigee environment.

        Args:
            payload (dict): The payload containing shared flow details.

        Returns:
            dict: The response from the API containing details of the created shared flow.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.post(f"{self.base_url}/shared-flows", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()

    def delete_shared_flow(self, shared_flow_id: str) -> Dict[str, Any]:
        """
        Deletes a shared flow by its ID.

        Args:
            shared_flow_id (str): The ID of the shared flow to delete.

        Returns:
            dict: The response from the API confirming the deletion.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.delete(f"{self.base_url}/shared-flows/{shared_flow_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def fetch_shared_flow_details(self, shared_flow_id: str) -> Dict[str, Any]:
        """
        Fetches details of a specific shared flow by its ID.

        Args:
            shared_flow_id (str): The ID of the shared flow to fetch details for.

        Returns:
            dict: The response from the API containing shared flow details.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.get(f"{self.base_url}/shared-flows/{shared_flow_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def list_shared_flows(self) -> Dict[str, Any]:
        """
        Lists all shared flows in the Apigee environment.

        Returns:
            dict: The response from the API containing a list of shared flows.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.get(f"{self.base_url}/shared-flows", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_shared_flow(self, shared_flow_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates an existing shared flow by its ID.

        Args:
            shared_flow_id (str): The ID of the shared flow to update.
            payload (dict): The payload containing updated shared flow details.

        Returns:
            dict: The response from the API containing details of the updated shared flow.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.put(f"{self.base_url}/shared-flows/{shared_flow_id}", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()