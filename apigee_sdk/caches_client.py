import requests

class CachesClient:
    """
    A client for managing caches in the Apigee API.

    This client provides methods to create, delete, fetch details, list, and update caches
    in an Apigee environment.

    Attributes:
        base_url (str): The base URL for the Apigee API.
        headers (dict): The headers used for API requests, including the authorization token.
    """

    def __init__(self, base_url, token):
        """
        Initializes the CachesClient with the base URL and authorization token.

        Args:
            base_url (str): The base URL for the Apigee API.
            token (str): The authorization token for accessing the API.
        """
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def create_cache(self, payload):
        """
        Creates a new cache in the Apigee environment.

        Args:
            payload (dict): The payload containing cache configuration details.

        Returns:
            dict: The response from the API containing details of the created cache.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.post(
            f"{self.base_url}/caches",
            headers={"Content-Type": "application/json", **self.headers},
            json=payload
        )
        response.raise_for_status()
        return response.json()

    def delete_cache(self, cache_id):
        """
        Deletes a cache by its ID.

        Args:
            cache_id (str): The ID of the cache to delete.

        Returns:
            dict: The response from the API confirming the deletion.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.delete(
            f"{self.base_url}/caches/{cache_id}",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def fetch_cache_details(self, cache_id):
        """
        Fetches details of a specific cache by its ID.

        Args:
            cache_id (str): The ID of the cache to fetch details for.

        Returns:
            dict: The response from the API containing cache details.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.get(
            f"{self.base_url}/caches/{cache_id}",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def list_caches(self):
        """
        Lists all caches in the Apigee environment.

        Returns:
            dict: The response from the API containing a list of caches.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.get(
            f"{self.base_url}/caches",
            headers=self.headers
        )
        response.raise_for_status()
        return response.json()

    def update_cache(self, cache_id, payload):
        """
        Updates an existing cache by its ID.

        Args:
            cache_id (str): The ID of the cache to update.
            payload (dict): The payload containing updated cache configuration details.

        Returns:
            dict: The response from the API containing details of the updated cache.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.put(
            f"{self.base_url}/caches/{cache_id}",
            headers={"Content-Type": "application/json", **self.headers},
            json=payload
        )
        response.raise_for_status()
        return response.json()