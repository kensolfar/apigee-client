import requests

class DevelopersClient:
    """
    Client to manage developers in Apigee Edge.

    This client provides methods to create, update, delete, and fetch details of developers.

    Attributes:
        base_url (str): The base URL for the Apigee API.
        headers (dict): The headers used for API requests, including the authorization token.
    """

    def __init__(self, base_url, token):
        """
        Initializes the DevelopersClient with the base URL and authorization token.

        Args:
            base_url (str): The base URL for the Apigee API.
            token (str): The authorization token for accessing the API.
        """
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}

    def create_developer(self, payload):
        """
        Creates a new developer in the Apigee environment.

        Args:
            payload (dict): The payload containing developer details.

        Returns:
            dict: The response from the API containing details of the created developer.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.post(f"{self.base_url}/developers", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()

    def delete_developer(self, developer_id):
        """
        Deletes a developer by their ID.

        Args:
            developer_id (str): The ID of the developer to delete.

        Returns:
            dict: The response from the API confirming the deletion.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.delete(f"{self.base_url}/developers/{developer_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def fetch_developer_details(self, developer_id):
        """
        Fetches details of a specific developer by their ID.

        Args:
            developer_id (str): The ID of the developer to fetch details for.

        Returns:
            dict: The response from the API containing developer details.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.get(f"{self.base_url}/developers/{developer_id}", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def list_developers(self):
        """
        Lists all developers in the Apigee environment.

        Returns:
            dict: The response from the API containing a list of developers.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.get(f"{self.base_url}/developers", headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_developer(self, developer_id, payload):
        """
        Updates an existing developer by their ID.

        Args:
            developer_id (str): The ID of the developer to update.
            payload (dict): The payload containing updated developer details.

        Returns:
            dict: The response from the API containing details of the updated developer.

        Raises:
            HTTPError: If the API request fails.
        """
        response = requests.put(f"{self.base_url}/developers/{developer_id}", headers={"Content-Type": "application/json", **self.headers}, json=payload)
        response.raise_for_status()
        return response.json()