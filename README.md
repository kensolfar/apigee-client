# Apigee Client SDK and CLI

This project provides a Python SDK to interact with the Apigee Management API, as well as a CLI that implements the SDK's functions.

## Project Structure

The project has the following structure:

```
README.md
requirements.txt
cli/
    __init__.py
    proxy_cli.py
sdk/
    __init__.py
    proxy_client.py
    kvm_client.py
    products_client.py
    shared_flows_client.py
    developers_client.py
    users_client.py
    user_roles_client.py
    keystores_client.py
    caches_client.py
tests/
    test_proxy_cli.py
    test_proxy_client.py
    test_kvm_client.py
    test_products_client.py
    test_shared_flows_client.py
    test_developers_client.py
    test_users_client.py
    test_user_roles_client.py
    test_keystores_client.py
    test_caches_client.py
```

- `README.md`: Project documentation.
- `requirements.txt`: List of project dependencies.
- `cli/`: Contains the CLI to interact with the SDK.
  - `proxy_cli.py`: CLI implementation.
- `sdk/`: Contains the SDK to interact with the Apigee Management API.
  - `proxy_client.py`: SDK client implementation.
  - `kvm_client.py`: SDK client for Key-Value Map (KVM) management.
  - `products_client.py`: SDK client for Products management.
  - `shared_flows_client.py`: SDK client for Shared Flows management.
  - `developers_client.py`: SDK client for Developers management.
  - `users_client.py`: SDK client for Users management.
  - `user_roles_client.py`: SDK client for User Roles management.
  - `keystores_client.py`: SDK client for Keystores management.
  - `caches_client.py`: SDK client for Caches management.
- `tests/`: Contains unit tests for the SDK and CLI.

## Installation

1. Clone this repository.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### CLI

The CLI allows interaction with the Apigee SDK. Below are some examples of available commands:

#### Proxy Subcommand

The `proxy` subcommand provides access to methods in the `ProxyClient` class. Use the method name directly to call a specific method dynamically.

##### Example: Create an API Proxy

```bash
apigee-client proxy create_api_proxy \
  --base-url https://api.enterprise.apigee.com \
  --token <BEARER_TOKEN> \
  --org <ORGANIZATION_NAME> \
  --payload '{"name": "example-proxy"}'
```

##### Example: Upload a Proxy Revision

```bash
apigee-client proxy upload_proxy_revision \
  --base-url https://api.enterprise.apigee.com \
  --token <BEARER_TOKEN> \
  --org <ORGANIZATION_NAME> \
  --api <API_NAME> \
  --payload '{"revision": "1"}'
```

##### Example: List Proxy Revisions

```bash
apigee-client proxy list_proxy_revisions \
  --base-url https://api.enterprise.apigee.com \
  --token <BEARER_TOKEN> \
  --org <ORGANIZATION_NAME> \
  --api <API_NAME>
```

##### Example: Deploy a Proxy Revision

```bash
apigee-client proxy deploy_proxy_revision \
  --base-url https://api.enterprise.apigee.com \
  --token <BEARER_TOKEN> \
  --org <ORGANIZATION_NAME> \
  --env <ENVIRONMENT> \
  --api <API_NAME> \
  --revision <REVISION_NUMBER>
```

#### Developer App Management

The `app` subcommand allows you to manage developer apps in Apigee Edge. Below are the available methods and their usage:

##### Usage

```bash
python cli/proxy_cli.py app <method> --base-url <BASE_URL> --token <TOKEN> [--app-id <APP_ID>] [--api-key-id <API_KEY_ID>] [--payload <PAYLOAD>]
```

##### Methods

- `add_api_key`: Adds an API key to a developer app.
  - Required options: `--app-id`, `--payload`
  - Example:
    ```bash
    python cli/proxy_cli.py app add_api_key --base-url https://api.example.com --token YOUR_TOKEN --app-id APP_ID --payload '{"key": "value"}'
    ```

- `approve_api_key`: Approves an API key for a developer app.
  - Required options: `--app-id`, `--api-key-id`
  - Example:
    ```bash
    python cli/proxy_cli.py app approve_api_key --base-url https://api.example.com --token YOUR_TOKEN --app-id APP_ID --api-key-id API_KEY_ID
    ```

- `create_app`: Creates a new developer app.
  - Required options: `--payload`
  - Example:
    ```bash
    python cli/proxy_cli.py app create_app --base-url https://api.example.com --token YOUR_TOKEN --payload '{"name": "new-app"}'
    ```

- `delete_app`: Deletes a developer app.
  - Required options: `--app-id`
  - Example:
    ```bash
    python cli/proxy_cli.py app delete_app --base-url https://api.example.com --token YOUR_TOKEN --app-id APP_ID
    ```

- `fetch_app_details`: Fetches details of a developer app.
  - Required options: `--app-id`
  - Example:
    ```bash
    python cli/proxy_cli.py app fetch_app_details --base-url https://api.example.com --token YOUR_TOKEN --app-id APP_ID
    ```

- `list_apps`: Lists all developer apps.
  - Example:
    ```bash
    python cli/proxy_cli.py app list_apps --base-url https://api.example.com --token YOUR_TOKEN
    ```

- `revoke_api_key`: Revokes an API key for a developer app.
  - Required options: `--app-id`, `--api-key-id`
  - Example:
    ```bash
    python cli/proxy_cli.py app revoke_api_key --base-url https://api.example.com --token YOUR_TOKEN --app-id APP_ID --api-key-id API_KEY_ID
    ```

- `update_app`: Updates a developer app.
  - Required options: `--app-id`, `--payload`
  - Example:
    ```bash
    python cli/proxy_cli.py app update_app --base-url https://api.example.com --token YOUR_TOKEN --app-id APP_ID --payload '{"name": "updated-app"}'
    ```

### SDK

Import the SDK into your Python project:

```python
from sdk.proxy_client import ProxyClient

client = ProxyClient(base_url="https://api.enterprise.apigee.com", token="your_token")
response = client.create_api_proxy(org="your_org", payload={"name": "example-proxy"}, bearer="your_token")
print(response)
```

## Key-Value Map (KVM) Management

The SDK now includes a `KVMClient` class for managing Key-Value Maps (KVMs) in Apigee. Below are the available methods and their usage:

### SDK Usage

Import the `KVMClient` into your Python project:

```python
from apigee_sdk.kvm_client import KVMClient

client = KVMClient(base_url="https://api.example.com", token="your_token")

# Create a new KVM
response = client.create_kvm(payload={"name": "example-kvm"})
print(response)

# Fetch details of a KVM
response = client.fetch_kvm_details(kvm_id="example-kvm-id")
print(response)

# List all KVMs
response = client.list_kvms()
print(response)

# Update a KVM
response = client.update_kvm(kvm_id="example-kvm-id", payload={"name": "updated-kvm"})
print(response)

# Delete a KVM
response = client.delete_kvm(kvm_id="example-kvm-id")
print(response)
```

## Products Management

The SDK includes a `ProductsClient` class for managing products in Apigee. Below are the available methods and their usage:

### SDK Usage

Import the `ProductsClient` into your Python project:

```python
from apigee_sdk.products_client import ProductsClient

client = ProductsClient(base_url="https://api.example.com", token="your_token")

# Create a new product
response = client.create_product(payload={"name": "example-product"})
print(response)

# Fetch details of a product
response = client.fetch_product_details(product_id="example-product-id")
print(response)

# List all products
response = client.list_products()
print(response)

# Update a product
response = client.update_product(product_id="example-product-id", payload={"name": "updated-product"})
print(response)

# Delete a product
response = client.delete_product(product_id="example-product-id")
print(response)
```

## Shared Flows Management

The SDK includes a `SharedFlowsClient` class for managing shared flows in Apigee. Below are the available methods and their usage:

### SDK Usage

Import the `SharedFlowsClient` into your Python project:

```python
from apigee_sdk.shared_flows_client import SharedFlowsClient

client = SharedFlowsClient(base_url="https://api.example.com", token="your_token")

# Create a new shared flow
response = client.create_shared_flow(payload={"name": "example-shared-flow"})
print(response)

# Fetch details of a shared flow
response = client.fetch_shared_flow_details(shared_flow_id="example-shared-flow-id")
print(response)

# List all shared flows
response = client.list_shared_flows()
print(response)

# Update a shared flow
response = client.update_shared_flow(shared_flow_id="example-shared-flow-id", payload={"name": "updated-shared-flow"})
print(response)

# Delete a shared flow
response = client.delete_shared_flow(shared_flow_id="example-shared-flow-id")
print(response)
```

## Developers Management

The SDK includes a `DevelopersClient` class for managing developers in Apigee. Below are the available methods and their usage:

### SDK Usage

Import the `DevelopersClient` into your Python project:

```python
from apigee_sdk.developers_client import DevelopersClient

client = DevelopersClient(base_url="https://api.example.com", token="your_token")

# Create a new developer
response = client.create_developer(payload={"email": "example@developer.com"})
print(response)

# Fetch details of a developer
response = client.fetch_developer_details(developer_id="example-developer-id")
print(response)

# List all developers
response = client.list_developers()
print(response)

# Update a developer
response = client.update_developer(developer_id="example-developer-id", payload={"email": "updated@developer.com"})
print(response)

# Delete a developer
response = client.delete_developer(developer_id="example-developer-id")
print(response)
```

## Users Management

The SDK includes a `UsersClient` class for managing users in Apigee. Below are the available methods and their usage:

### SDK Usage

Import the `UsersClient` into your Python project:

```python
from apigee_sdk.users_client import UsersClient

client = UsersClient(base_url="https://api.example.com", token="your_token")

# Create a new user
response = client.create_user(payload={"username": "example-user"})
print(response)

# Fetch details of a user
response = client.fetch_user_details(user_id="example-user-id")
print(response)

# List all users
response = client.list_users()
print(response)

# Update a user
response = client.update_user(user_id="example-user-id", payload={"username": "updated-user"})
print(response)

# Delete a user
response = client.delete_user(user_id="example-user-id")
print(response)
```

## User Roles Management

The SDK includes a `UserRolesClient` class for managing user roles in Apigee. Below are the available methods and their usage:

### SDK Usage

Import the `UserRolesClient` into your Python project:

```python
from apigee_sdk.user_roles_client import UserRolesClient

client = UserRolesClient(base_url="https://api.example.com", token="your_token")

# Create a new user role
response = client.create_user_role(payload={"roleName": "example-role"})
print(response)

# Fetch details of a user role
response = client.fetch_user_role_details(role_id="example-role-id")
print(response)

# List all user roles
response = client.list_user_roles()
print(response)

# Update a user role
response = client.update_user_role(role_id="example-role-id", payload={"roleName": "updated-role"})
print(response)

# Delete a user role
response = client.delete_user_role(role_id="example-role-id")
print(response)
```

## Keystores Management

The SDK includes a `KeystoresClient` class for managing keystores in Apigee. Below are the available methods and their usage:

### SDK Usage

Import the `KeystoresClient` into your Python project:

```python
from apigee_sdk.keystores_client import KeystoresClient

client = KeystoresClient(base_url="https://api.example.com", token="your_token")

# Create a new keystore
response = client.create_keystore(payload={"name": "example-keystore"})
print(response)

# Fetch details of a keystore
response = client.fetch_keystore_details(keystore_id="example-keystore-id")
print(response)

# List all keystores
response = client.list_keystores()
print(response)

# Update a keystore
response = client.update_keystore(keystore_id="example-keystore-id", payload={"name": "updated-keystore"})
print(response)

# Delete a keystore
response = client.delete_keystore(keystore_id="example-keystore-id")
print(response)
```

## Caches Management

The SDK includes a `CachesClient` class for managing caches in Apigee. Below are the available methods and their usage:

### SDK Usage

Import the `CachesClient` into your Python project:

```python
from apigee_sdk.caches_client import CachesClient

client = CachesClient(base_url="https://api.example.com", token="your_token")

# Create a new cache
response = client.create_cache(payload={"name": "example-cache"})
print(response)

# Fetch details of a cache
response = client.fetch_cache_details(cache_id="example-cache-id")
print(response)

# List all caches
response = client.list_caches()
print(response)

# Update a cache
response = client.update_cache(cache_id="example-cache-id", payload={"name": "updated-cache"})
print(response)

# Delete a cache
response = client.delete_cache(cache_id="example-cache-id")
print(response)
```

### Unit Tests

The functionality of the `KVMClient`, `ProductsClient`, `SharedFlowsClient`, `DevelopersClient`, `UsersClient`, `UserRolesClient`, `KeystoresClient`, and `CachesClient` is covered by unit tests in their respective test files. To run the tests, use the following commands:

```bash
pytest tests/test_kvm_client.py
pytest tests/test_products_client.py
pytest tests/test_shared_flows_client.py
pytest tests/test_developers_client.py
pytest tests/test_users_client.py
pytest tests/test_user_roles_client.py
pytest tests/test_keystores_client.py
pytest tests/test_caches_client.py
```

## Contributing

If you wish to contribute, please open an issue or a pull request.