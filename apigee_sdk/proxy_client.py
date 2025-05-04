import requests

class ProxyClient:
    """Client to interact with the Apigee Management API."""
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token

    def _handle_request_errors(self, response):
        """Handles common HTTP request errors."""
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
        """Creates a new API Proxy."""
        url = f"{self.base_url}/v1/organizations/{org}/apis"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.post(url, headers=headers, json=payload)
        self._handle_request_errors(response)
        return response.json()

    def upload_proxy_revision(self, org, api, payload, bearer):
        """Uploads a new revision of the API Proxy."""
        url = f"{self.base_url}/v1/organizations/{org}/apis/{api}/revisions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.post(url, headers=headers, json=payload)
        self._handle_request_errors(response)
        return response.json()

    def list_proxy_revisions(self, org, api, bearer):
        """Lists all available revisions for an API Proxy."""
        url = f"{self.base_url}/v1/organizations/{org}/apis/{api}/revisions"
        headers = {
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.get(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def deploy_proxy_revision(self, org, env, api, revision, bearer):
        """Deploys a specific revision of the API Proxy to an environment."""
        url = f"{self.base_url}/v1/organizations/{org}/environments/{env}/apis/{api}/revisions/{revision}/deployments"
        headers = {
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.post(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def get_deployment_status(self, org, env, api, bearer):
        """Checks the deployment status of the API Proxy in an environment."""
        url = f"{self.base_url}/v1/organizations/{org}/environments/{env}/apis/{api}/deployments"
        headers = {
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.get(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def delete_deployment(self, org, env, api, revision, bearer):
        """Deletes the deployment of a specific revision of the API Proxy."""
        url = f"{self.base_url}/v1/organizations/{org}/environments/{env}/apis/{api}/revisions/{revision}/deployments"
        headers = {
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.delete(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def update_proxy_policies(self, org, api, revision, payload, bearer):
        """Updates the policies of the API Proxy."""
        url = f"{self.base_url}/v1/organizations/{org}/apis/{api}/revisions/{revision}/policies"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.put(url, headers=headers, json=payload)
        self._handle_request_errors(response)
        return response.json()

    def get_proxy_revision_details(self, org, api, revision, bearer):
        """Gets the details of a specific revision of the API Proxy."""
        url = f"{self.base_url}/v1/organizations/{org}/apis/{api}/revisions/{revision}"
        headers = {
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.get(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def list_apis(self, org, bearer):
        """Lists all API Proxies in the organization."""
        url = f"{self.base_url}/v1/organizations/{org}/apis"
        headers = {
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.get(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def delete_api(self, org, api, bearer):
        """Deletes an API Proxy from the organization."""
        url = f"{self.base_url}/v1/organizations/{org}/apis/{api}"
        headers = {
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.delete(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def start_debug_session(self, org, env, api, revision, bearer):
        """Starts a debug session for a deployed API Proxy."""
        url = f"{self.base_url}/v1/organizations/{org}/environments/{env}/apis/{api}/revisions/{revision}/debugsessions"
        headers = {
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.post(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def get_api_metrics(self, org, env, bearer):
        """Gets usage and performance metrics for the API Proxy."""
        url = f"{self.base_url}/v1/organizations/{org}/environments/{env}/stats/apis"
        headers = {
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.get(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def create_api_product(self, org, payload, bearer):
        """Creates an API product associated with the API Proxy."""
        url = f"{self.base_url}/v1/organizations/{org}/apiproducts"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.post(url, headers=headers, json=payload)
        self._handle_request_errors(response)
        return response.json()

    def update_api_product(self, org, product, payload, bearer):
        """Updates an API product to associate it with an API Proxy."""
        url = f"{self.base_url}/v1/organizations/{org}/apiproducts/{product}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.put(url, headers=headers, json=payload)
        self._handle_request_errors(response)
        return response.json()

    def promote_revision_to_production(self, org, api, revision, bearer):
        """Promotes a revision of the API Proxy to the production environment."""
        url = f"{self.base_url}/v1/organizations/{org}/environments/prod/apis/{api}/revisions/{revision}/deployments"
        headers = {
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.post(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()

    def delete_proxy_revision(self, org, api, revision, bearer):
        """Deletes a specific revision of the API Proxy."""
        url = f"{self.base_url}/v1/organizations/{org}/apis/{api}/revisions/{revision}"
        headers = {
            "Authorization": f"Bearer {bearer}"
        }
        response = requests.delete(url, headers=headers)
        self._handle_request_errors(response)
        return response.json()