from typing import Dict, Any
import requests

class ProductsClient:
    """
    Client to manage API products in Apigee Edge.

    This client provides methods to create, update, delete, and fetch details of API products.

    Attributes:
        base_url (str): The base URL for the Apigee API.
        headers (dict): The headers used for API requests, including the authorization token.
    """

    def __init__(self, base_url: str, token: str) -> None:
        """
        Initializes the ProductsClient with the base URL and authorization token.

        Args:
            base_url (str): The base URL for the Apigee API.
            token (str): The authorization token for accessing the API.
        """
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def create_product(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new API product in the Apigee environment.

        Args:
            payload (dict): The payload containing API product details.

        Returns:
            dict: The response from the API containing details of the created product.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.post(f"{self.base_url}/products", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()

    def delete_product(self, product_id: str) -> Dict[str, Any]:
        """
        Deletes an API product by its ID.

        Args:
            product_id (str): The ID of the API product to delete.

        Returns:
            dict: The response from the API confirming the deletion.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.delete(f"{self.base_url}/products/{product_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def fetch_product_details(self, product_id: str) -> Dict[str, Any]:
        """
        Fetches details of a specific API product by its ID.

        Args:
            product_id (str): The ID of the API product to fetch details for.

        Returns:
            dict: The response from the API containing product details.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.get(f"{self.base_url}/products/{product_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def list_products(self) -> Dict[str, Any]:
        """
        Lists all API products in the Apigee environment.

        Returns:
            dict: The response from the API containing a list of API products.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.get(f"{self.base_url}/products", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_product(self, product_id: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates an existing API product by its ID.

        Args:
            product_id (str): The ID of the API product to update.
            payload (dict): The payload containing updated product details.

        Returns:
            dict: The response from the API containing details of the updated product.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.put(f"{self.base_url}/products/{product_id}", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()