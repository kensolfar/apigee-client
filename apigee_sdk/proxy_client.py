import requests

class ProxyClient:
    """
    Client to interact with the Apigee Management API.

    This client provides methods to manage API proxies, including creating, uploading revisions,
    deploying, fetching details, and managing API products and metrics.

    Attributes:
        base_url (str): The base URL for the Apigee API.
        token (str): The authorization token for accessing the API.
    """

    def __init__(self, base_url, token):
        """
        Initializes the ProxyClient with the base URL and authorization token.

        Args:
            base_url (str): The base URL for the Apigee API.
            token (str): The authorization token for accessing the API.
        """
        self.base_url = base_url
        self.token = token

    def _handle_request_errors(self, response):
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

    def create_api_proxy(self, org, payload, bearer):
        """
        Creates a new API Proxy.

        Args:
            org (str): The organization name.
            payload (dict): The payload containing API proxy details.
            bearer (str): The bearer token for authorization.

        Returns:
            dict: The response from the API containing details of the created proxy.

        Raises:
            HTTPError: If the API request fails due to an HTTP error.
        """
        url = f"{self.base_url}/v1/organizations/{org}/apis"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.post(url, headers=headers, json=payload)
        self._handle_request_errors(response)
        return response.json()

    def upload_proxy_revision(self, org, api, payload, bearer):
        """
        Uploads a new revision of the API Proxy.

        Args:
            org (str): The organization name.
            api (str): The API proxy name.
            payload (dict): The payload containing revision details.
            bearer (str): The bearer token for authorization.

        Returns:
            dict: The response from the API containing details of the uploaded revision.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/v1/organizations/{org}/apis/{api}/revisions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.post(url, headers=headers, json=payload)
        self._handle_request_errors(response)
        return response.json()

    def list_proxy_revisions(self, org, api, bearer):
        """
        Lists all available revisions for an API Proxy.

        Args:
            org (str): The organization name.
            api (str): The API proxy name.
            bearer (str): The bearer token for authorization.

        Returns:
            dict: The response from the API containing a list of revisions.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/v1/organizations/{org}/apis/{api}/revisions"
        headers = {
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.get(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def deploy_proxy_revision(self, org, env, api, revision, bearer):
        """
        Deploys a specific revision of the API Proxy to an environment.

        Args:
            org (str): The organization name.
            env (str): The environment name.
            api (str): The API proxy name.
            revision (str): The revision number to deploy.
            bearer (str): The bearer token for authorization.

        Returns:
            dict: The response from the API confirming the deployment.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/v1/organizations/{org}/environments/{env}/apis/{api}/revisions/{revision}/deployments"
        headers = {
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.post(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def get_deployment_status(self, org, env, api, bearer):
        """
        Checks the deployment status of the API Proxy in an environment.

        Args:
            org (str): The organization name.
            env (str): The environment name.
            api (str): The API proxy name.
            bearer (str): The bearer token for authorization.

        Returns:
            dict: The response from the API containing deployment status.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/v1/organizations/{org}/environments/{env}/apis/{api}/deployments"
        headers = {
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.get(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def delete_deployment(self, org, env, api, revision, bearer):
        """
        Deletes the deployment of a specific revision of the API Proxy.

        Args:
            org (str): The organization name.
            env (str): The environment name.
            api (str): The API proxy name.
            revision (str): The revision number to delete.
            bearer (str): The bearer token for authorization.

        Returns:
            dict: The response from the API confirming the deletion.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/v1/organizations/{org}/environments/{env}/apis/{api}/revisions/{revision}/deployments"
        headers = {
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.delete(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def update_proxy_policies(self, org, api, revision, payload, bearer):
        """
        Updates the policies of the API Proxy.

        Args:
            org (str): The organization name.
            api (str): The API proxy name.
            revision (str): The revision number.
            payload (dict): The payload containing updated policy details.
            bearer (str): The bearer token for authorization.

        Returns:
            dict: The response from the API confirming the update.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/v1/organizations/{org}/apis/{api}/revisions/{revision}/policies"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.put(url, headers=headers, json=payload)
        self._handle_request_errors(response)
        return response.json()

    def get_proxy_revision_details(self, org, api, revision, bearer):
        """
        Gets the details of a specific revision of the API Proxy.

        Args:
            org (str): The organization name.
            api (str): The API proxy name.
            revision (str): The revision number.
            bearer (str): The bearer token for authorization.

        Returns:
            dict: The response from the API containing revision details.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/v1/organizations/{org}/apis/{api}/revisions/{revision}"
        headers = {
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.get(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def list_apis(self, org, bearer):
        """
        Lists all API Proxies in the organization.

        Args:
            org (str): The organization name.
            bearer (str): The bearer token for authorization.

        Returns:
            dict: The response from the API containing a list of API proxies.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/v1/organizations/{org}/apis"
        headers = {
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.get(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def delete_api(self, org, api, bearer):
        """
        Deletes an API Proxy from the organization.

        Args:
            org (str): The organization name.
            api (str): The API proxy name.
            bearer (str): The bearer token for authorization.

        Returns:
            dict: The response from the API confirming the deletion.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/v1/organizations/{org}/apis/{api}"
        headers = {
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.delete(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def start_debug_session(self, org, env, api, revision, bearer):
        """
        Starts a debug session for a deployed API Proxy.

        Args:
            org (str): The organization name.
            env (str): The environment name.
            api (str): The API proxy name.
            revision (str): The revision number.
            bearer (str): The bearer token for authorization.

        Returns:
            dict: The response from the API containing debug session details.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/v1/organizations/{org}/environments/{env}/apis/{api}/revisions/{revision}/debugsessions"
        headers = {
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.post(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def get_api_metrics(self, org, env, bearer):
        """
        Gets usage and performance metrics for the API Proxy.

        Args:
            org (str): The organization name.
            env (str): The environment name.
            bearer (str): The bearer token for authorization.

        Returns:
            dict: The response from the API containing metrics.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/v1/organizations/{org}/environments/{env}/stats/apis"
        headers = {
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.get(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def create_api_product(self, org, payload, bearer):
        """
        Creates an API product associated with the API Proxy.

        Args:
            org (str): The organization name.
            payload (dict): The payload containing API product details.
            bearer (str): The bearer token for authorization.

        Returns:
            dict: The response from the API containing details of the created product.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/v1/organizations/{org}/apiproducts"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.post(url, headers=headers, json=payload)
        self._handle_request_errors(response)
        return response.json()

    def update_api_product(self, org, product, payload, bearer):
        """
        Updates an API product to associate it with an API Proxy.

        Args:
            org (str): The organization name.
            product (str): The API product name.
            payload (dict): The payload containing updated product details.
            bearer (str): The bearer token for authorization.

        Returns:
            dict: The response from the API confirming the update.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/v1/organizations/{org}/apiproducts/{product}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.put(url, headers=headers, json=payload)
        self._handle_request_errors(response)
        return response.json()

    def promote_revision_to_production(self, org, api, revision, bearer):
        """
        Promotes a revision of the API Proxy to the production environment.

        Args:
            org (str): The organization name.
            api (str): The API proxy name.
            revision (str): The revision number to promote.
            bearer (str): The bearer token for authorization.

        Returns:
            dict: The response from the API confirming the promotion.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/v1/organizations/{org}/environments/prod/apis/{api}/revisions/{revision}/deployments"
        headers = {
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.post(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def delete_proxy_revision(self, org, api, revision, bearer):
        """
        Deletes a specific revision of the API Proxy.

        Args:
            org (str): The organization name.
            api (str): The API proxy name.
            revision (str): The revision number to delete.
            bearer (str): The bearer token for authorization.

        Returns:
            dict: The response from the API confirming the deletion.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/v1/organizations/{org}/apis/{api}/revisions/{revision}"
        headers = {
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.delete(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()