from typing import Dict, Any
import requests

class KVMClient:
    """
    Client to manage Key-Value Maps (KVMs) in Apigee Edge.

    This client provides methods to create, update, delete, and fetch details of KVMs.

    Attributes:
        base_url (str): The base URL for the Apigee API.
        headers (dict): The headers used for API requests, including the authorization token.
    """

    def __init__(self, base_url: str, token: str) -> None:
        """
        Initializes the KVMClient with the base URL and authorization token.

        Args:
            base_url (str): The base URL for the Apigee API.
            token (str): The authorization token for accessing the API.
        """
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def create_kvm(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new Key-Value Map (KVM) in the Apigee environment.

        Args:
            payload (dict): The payload containing KVM details.

        Returns:
            dict: The response from the API containing details of the created KVM.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.post(f"{self.base_url}/kvms", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()

    def delete_kvm(self, kvm_id: str) -> Dict[str, Any]:
        """
        Deletes a Key-Value Map (KVM) by its ID.

        Args:
            kvm_id (str): The ID of the KVM to delete.

        Returns:
            dict: The response from the API confirming the deletion.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.delete(f"{self.base_url}/kvms/{kvm_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def fetch_kvm_details(self, kvm_id: str) -> Dict[str, Any]:
        """
        Fetches details of a specific Key-Value Map (KVM) by its ID.

        Args:
            kvm_id (str): The ID of the KVM to fetch details for.

        Returns:
            dict: The response from the API containing KVM details.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.get(f"{self.base_url}/kvms/{kvm_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def list_kvms(self) -> Dict[str, Any]:
        """
        Lists all Key-Value Maps (KVMs) in the Apigee environment.

        Returns:
            dict: The response from the API containing a list of KVMs.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.get(f"{self.base_url}/kvms", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_kvm(self, kvm_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates an existing Key-Value Map (KVM) by its ID.

        Args:
            kvm_id (str): The ID of the KVM to update.
            payload (dict): The payload containing updated KVM details.

        Returns:
            dict: The response from the API containing details of the updated KVM.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.put(f"{self.base_url}/kvms/{kvm_id}", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()