import click
from apigee_sdk.proxy_client import ProxyClient 
from apigee_sdk.developer_app_client import DeveloperAppClient

@click.group()
def cli():
    """CLI to interact with the Apigee SDK."""
    pass

@cli.group()
def proxy():
    """Subcommand to interact with API proxies."""
    pass

@proxy.command()
@click.argument('action', required=True)
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--org', help='Apigee organization name (if applicable).')
@click.option('--api', help='API Proxy name (if applicable).')
@click.option('--revision', help='Revision number (if applicable).')
@click.option('--env', help='Environment (if applicable).')
@click.option('--payload', help='Payload in JSON format (if applicable).')
def proxy_action(action, base_url, token, org, api, revision, env, payload):
    """Perform an action using the ProxyClient."""
    client = ProxyClient(base_url, token)
    try:
        func = getattr(client, action, None)
        if not callable(func):
            click.echo(f"Error: Action '{action}' not found in ProxyClient.", err=True)
            raise SystemExit(2)

        kwargs = {}
        if org:
            kwargs['org'] = org
        if api:
            kwargs['api'] = api
        if revision:
            kwargs['revision'] = revision
        if env:
            kwargs['env'] = env
        if payload:
            import json
            kwargs['payload'] = json.loads(payload)

        response = func(**kwargs)
        click.echo(response)
    except Exception as e:
        click.echo(f"Error executing action '{action}': {e}", err=True)
        raise SystemExit(1)

@proxy.command("create-api-proxy")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--org', required=True, help='Apigee organization name.')
@click.option('--payload', required=True, help='Payload in JSON format.')
def create_api_proxy(base_url, token, org, payload):
    """Create a new API Proxy."""
    from apigee_sdk.proxy_client import ProxyClient

    client = ProxyClient(base_url, token)
    try:
        import json
        response = client.create_api_proxy(org, json.loads(payload), token)
        click.echo(response)
    except Exception as e:
        click.echo(f"Error creating API Proxy: {e}", err=True)
        raise SystemExit(1)

@cli.group()
def app():
    """Subcommand to interact with developer apps."""
    pass

@app.command()
@click.argument('action', required=True)
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--app-id', help='Developer app ID (if applicable).')
@click.option('--api-key-id', help='API key ID (if applicable).')
@click.option('--payload', help='Payload in JSON format (if applicable).')
def app_action(action, base_url, token, app_id, api_key_id, payload):
    """Perform an action using the DeveloperAppClient."""
    client = DeveloperAppClient(base_url, token)
    try:
        func = getattr(client, action, None)
        if not callable(func):
            click.echo(f"Error: Action '{action}' not found in DeveloperAppClient.", err=True)
            raise SystemExit(2)

        kwargs = {}
        if app_id:
            kwargs['app_id'] = app_id
        if api_key_id:
            kwargs['api_key_id'] = api_key_id
        if payload:
            import json
            kwargs['payload'] = json.loads(payload)

        response = func(**kwargs)
        click.echo(response)
    except Exception as e:
        click.echo(f"Error executing action '{action}': {e}", err=True)
        raise SystemExit(1)

@app.command("create-app")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--payload', required=True, help='Payload in JSON format.')
def create_app(base_url, token, payload):
    """Create a new developer app."""
    from apigee_sdk.developer_app_client import DeveloperAppClient

    client = DeveloperAppClient(base_url, token)
    try:
        import json
        response = client.create_app(json.loads(payload))
        click.echo(response)
    except Exception as e:
        click.echo(f"Error creating app: {e}", err=True)
        raise SystemExit(1)

@cli.group()
def kvm():
    """Subcommand to interact with Key-Value Maps (KVMs)."""
    pass

@kvm.command("create-kvm")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--payload', required=True, help='Payload in JSON format.')
def create_kvm(base_url, token, payload):
    """Create a new Key-Value Map (KVM)."""
    from apigee_sdk.kvm_client import KVMClient

    client = KVMClient(base_url, token)
    try:
        import json
        response = client.create_kvm(json.loads(payload))
        click.echo(response)
    except Exception as e:
        click.echo(f"Error creating KVM: {e}", err=True)
        raise SystemExit(1)

@kvm.command("delete-kvm")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--kvm-id', required=True, help='KVM ID to delete.')
def delete_kvm(base_url, token, kvm_id):
    """Delete a Key-Value Map (KVM)."""
    from apigee_sdk.kvm_client import KVMClient

    client = KVMClient(base_url, token)
    try:
        response = client.delete_kvm(kvm_id)
        click.echo(response)
    except Exception as e:
        click.echo(f"Error deleting KVM: {e}", err=True)
        raise SystemExit(1)

@kvm.command("fetch-kvm-details")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--kvm-id', required=True, help='KVM ID to fetch details for.')
def fetch_kvm_details(base_url, token, kvm_id):
    """Fetch details of a Key-Value Map (KVM)."""
    from apigee_sdk.kvm_client import KVMClient

    client = KVMClient(base_url, token)
    try:
        response = client.fetch_kvm_details(kvm_id)
        click.echo(response)
    except Exception as e:
        click.echo(f"Error fetching KVM details: {e}", err=True)
        raise SystemExit(1)

@kvm.command("list-kvms")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
def list_kvms(base_url, token):
    """List all Key-Value Maps (KVMs)."""
    from apigee_sdk.kvm_client import KVMClient

    client = KVMClient(base_url, token)
    try:
        response = client.list_kvms()
        click.echo(response)
    except Exception as e:
        click.echo(f"Error listing KVMs: {e}", err=True)
        raise SystemExit(1)

@kvm.command("update-kvm")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--kvm-id', required=True, help='KVM ID to update.')
@click.option('--payload', required=True, help='Payload in JSON format.')
def update_kvm(base_url, token, kvm_id, payload):
    """Update a Key-Value Map (KVM)."""
    from apigee_sdk.kvm_client import KVMClient

    client = KVMClient(base_url, token)
    try:
        import json
        response = client.update_kvm(kvm_id, json.loads(payload))
        click.echo(response)
    except Exception as e:
        click.echo(f"Error updating KVM: {e}", err=True)
        raise SystemExit(1)

@cli.group()
def developers():
    """Subcommand to interact with Developers."""
    pass

@developers.command("create-developer")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--payload', required=True, help='Payload in JSON format.')
def create_developer(base_url, token, payload):
    """Create a new Developer."""
    from apigee_sdk.developers_client import DevelopersClient

    client = DevelopersClient(base_url, token)
    try:
        import json
        response = client.create_developer(json.loads(payload))
        click.echo(response)
    except Exception as e:
        click.echo(f"Error creating Developer: {e}", err=True)
        raise SystemExit(1)

@developers.command("delete-developer")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--developer-id', required=True, help='Developer ID to delete.')
def delete_developer(base_url, token, developer_id):
    """Delete a Developer."""
    from apigee_sdk.developers_client import DevelopersClient

    client = DevelopersClient(base_url, token)
    try:
        response = client.delete_developer(developer_id)
        click.echo(response)
    except Exception as e:
        click.echo(f"Error deleting Developer: {e}", err=True)
        raise SystemExit(1)

@developers.command("fetch-developer-details")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--developer-id', required=True, help='Developer ID to fetch details for.')
def fetch_developer_details(base_url, token, developer_id):
    """Fetch details of a Developer."""
    from apigee_sdk.developers_client import DevelopersClient

    client = DevelopersClient(base_url, token)
    try:
        response = client.fetch_developer_details(developer_id)
        click.echo(response)
    except Exception as e:
        click.echo(f"Error fetching Developer details: {e}", err=True)
        raise SystemExit(1)

@developers.command("list-developers")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
def list_developers(base_url, token):
    """List all Developers."""
    from apigee_sdk.developers_client import DevelopersClient

    client = DevelopersClient(base_url, token)
    try:
        response = client.list_developers()
        click.echo(response)
    except Exception as e:
        click.echo(f"Error listing Developers: {e}", err=True)
        raise SystemExit(1)

@developers.command("update-developer")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--developer-id', required=True, help='Developer ID to update.')
@click.option('--payload', required=True, help='Payload in JSON format.')
def update_developer(base_url, token, developer_id, payload):
    """Update a Developer."""
    from apigee_sdk.developers_client import DevelopersClient

    client = DevelopersClient(base_url, token)
    try:
        import json
        response = client.update_developer(developer_id, json.loads(payload))
        click.echo(response)
    except Exception as e:
        click.echo(f"Error updating Developer: {e}", err=True)
        raise SystemExit(1)

@cli.group()
def users():
    """Subcommand to interact with Users."""
    pass

@users.command("create-user")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--payload', required=True, help='Payload in JSON format.')
def create_user(base_url, token, payload):
    """Create a new User."""
    from apigee_sdk.users_client import UsersClient

    client = UsersClient(base_url, token)
    try:
        import json
        response = client.create_user(json.loads(payload))
        click.echo(response)
    except Exception as e:
        click.echo(f"Error creating User: {e}", err=True)
        raise SystemExit(1)

@users.command("delete-user")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--user-id', required=True, help='User ID to delete.')
def delete_user(base_url, token, user_id):
    """Delete a User."""
    from apigee_sdk.users_client import UsersClient

    client = UsersClient(base_url, token)
    try:
        response = client.delete_user(user_id)
        click.echo(response)
    except Exception as e:
        click.echo(f"Error deleting User: {e}", err=True)
        raise SystemExit(1)

@users.command("fetch-user-details")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--user-id', required=True, help='User ID to fetch details for.')
def fetch_user_details(base_url, token, user_id):
    """Fetch details of a User."""
    from apigee_sdk.users_client import UsersClient

    client = UsersClient(base_url, token)
    try:
        response = client.fetch_user_details(user_id)
        click.echo(response)
    except Exception as e:
        click.echo(f"Error fetching User details: {e}", err=True)
        raise SystemExit(1)

@users.command("list-users")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
def list_users(base_url, token):
    """List all Users."""
    from apigee_sdk.users_client import UsersClient

    client = UsersClient(base_url, token)
    try:
        response = client.list_users()
        click.echo(response)
    except Exception as e:
        click.echo(f"Error listing Users: {e}", err=True)
        raise SystemExit(1)

@users.command("update-user")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--user-id', required=True, help='User ID to update.')
@click.option('--payload', required=True, help='Payload in JSON format.')
def update_user(base_url, token, user_id, payload):
    """Update a User."""
    from apigee_sdk.users_client import UsersClient

    client = UsersClient(base_url, token)
    try:
        import json
        response = client.update_user(user_id, json.loads(payload))
        click.echo(response)
    except Exception as e:
        click.echo(f"Error updating User: {e}", err=True)
        raise SystemExit(1)

@cli.group()
def user_roles():
    """Subcommand to interact with User Roles."""
    pass

@user_roles.command("create-user-role")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--payload', required=True, help='Payload in JSON format.')
def create_user_role(base_url, token, payload):
    """Create a new User Role."""
    from apigee_sdk.user_roles_client import UserRolesClient

    client = UserRolesClient(base_url, token)
    try:
        import json
        response = client.create_user_role(json.loads(payload))
        click.echo(response)
    except Exception as e:
        click.echo(f"Error creating User Role: {e}", err=True)
        raise SystemExit(1)

@user_roles.command("delete-user-role")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--role-id', required=True, help='Role ID to delete.')
def delete_user_role(base_url, token, role_id):
    """Delete a User Role."""
    from apigee_sdk.user_roles_client import UserRolesClient

    client = UserRolesClient(base_url, token)
    try:
        response = client.delete_user_role(role_id)
        click.echo(response)
    except Exception as e:
        click.echo(f"Error deleting User Role: {e}", err=True)
        raise SystemExit(1)

@user_roles.command("fetch-user-role-details")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--role-id', required=True, help='Role ID to fetch details for.')
def fetch_user_role_details(base_url, token, role_id):
    """Fetch details of a User Role."""
    from apigee_sdk.user_roles_client import UserRolesClient

    client = UserRolesClient(base_url, token)
    try:
        response = client.fetch_user_role_details(role_id)
        click.echo(response)
    except Exception as e:
        click.echo(f"Error fetching User Role details: {e}", err=True)
        raise SystemExit(1)

@user_roles.command("list-user-roles")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
def list_user_roles(base_url, token):
    """List all User Roles."""
    from apigee_sdk.user_roles_client import UserRolesClient

    client = UserRolesClient(base_url, token)
    try:
        response = client.list_user_roles()
        click.echo(response)
    except Exception as e:
        click.echo(f"Error listing User Roles: {e}", err=True)
        raise SystemExit(1)

@user_roles.command("update-user-role")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--role-id', required=True, help='Role ID to update.')
@click.option('--payload', required=True, help='Payload in JSON format.')
def update_user_role(base_url, token, role_id, payload):
    """Update a User Role."""
    from apigee_sdk.user_roles_client import UserRolesClient

    client = UserRolesClient(base_url, token)
    try:
        import json
        response = client.update_user_role(role_id, json.loads(payload))
        click.echo(response)
    except Exception as e:
        click.echo(f"Error updating User Role: {e}", err=True)
        raise SystemExit(1)

@cli.group()
def keystores():
    """Subcommand to interact with Keystores."""
    pass

@keystores.command("create-keystore")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--payload', required=True, help='Payload in JSON format.')
def create_keystore(base_url, token, payload):
    """Create a new Keystore."""
    from apigee_sdk.keystores_client import KeystoresClient

    client = KeystoresClient(base_url, token)
    try:
        import json
        response = client.create_keystore(json.loads(payload))
        click.echo(response)
    except Exception as e:
        click.echo(f"Error creating Keystore: {e}", err=True)
        raise SystemExit(1)

@keystores.command("delete-keystore")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--keystore-id', required=True, help='Keystore ID to delete.')
def delete_keystore(base_url, token, keystore_id):
    """Delete a Keystore."""
    from apigee_sdk.keystores_client import KeystoresClient

    client = KeystoresClient(base_url, token)
    try:
        response = client.delete_keystore(keystore_id)
        click.echo(response)
    except Exception as e:
        click.echo(f"Error deleting Keystore: {e}", err=True)
        raise SystemExit(1)

@keystores.command("fetch-keystore-details")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--keystore-id', required=True, help='Keystore ID to fetch details for.')
def fetch_keystore_details(base_url, token, keystore_id):
    """Fetch details of a Keystore."""
    from apigee_sdk.keystores_client import KeystoresClient

    client = KeystoresClient(base_url, token)
    try:
        response = client.fetch_keystore_details(keystore_id)
        click.echo(response)
    except Exception as e:
        click.echo(f"Error fetching Keystore details: {e}", err=True)
        raise SystemExit(1)

@keystores.command("list-keystores")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
def list_keystores(base_url, token):
    """List all Keystores."""
    from apigee_sdk.keystores_client import KeystoresClient

    client = KeystoresClient(base_url, token)
    try:
        response = client.list_keystores()
        click.echo(response)
    except Exception as e:
        click.echo(f"Error listing Keystores: {e}", err=True)
        raise SystemExit(1)

@keystores.command("update-keystore")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--keystore-id', required=True, help='Keystore ID to update.')
@click.option('--payload', required=True, help='Payload in JSON format.')
def update_keystore(base_url, token, keystore_id, payload):
    """Update a Keystore."""
    from apigee_sdk.keystores_client import KeystoresClient

    client = KeystoresClient(base_url, token)
    try:
        import json
        response = client.update_keystore(keystore_id, json.loads(payload))
        click.echo(response)
    except Exception as e:
        click.echo(f"Error updating Keystore: {e}", err=True)
        raise SystemExit(1)

@cli.group()
def caches():
    """Subcommand to interact with Caches."""
    pass

@caches.command("create-cache")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--payload', required=True, help='Payload in JSON format.')
def create_cache(base_url, token, payload):
    """Create a new Cache."""
    from apigee_sdk.caches_client import CachesClient

    client = CachesClient(base_url, token)
    try:
        import json
        response = client.create_cache(json.loads(payload))
        click.echo(response)
    except Exception as e:
        click.echo(f"Error creating Cache: {e}", err=True)
        raise SystemExit(1)

@caches.command("delete-cache")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--cache-id', required=True, help='Cache ID to delete.')
def delete_cache(base_url, token, cache_id):
    """Delete a Cache."""
    from apigee_sdk.caches_client import CachesClient

    client = CachesClient(base_url, token)
    try:
        response = client.delete_cache(cache_id)
        click.echo(response)
    except Exception as e:
        click.echo(f"Error deleting Cache: {e}", err=True)
        raise SystemExit(1)

@caches.command("fetch-cache-details")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--cache-id', required=True, help='Cache ID to fetch details for.')
def fetch_cache_details(base_url, token, cache_id):
    """Fetch details of a Cache."""
    from apigee_sdk.caches_client import CachesClient

    client = CachesClient(base_url, token)
    try:
        response = client.fetch_cache_details(cache_id)
        click.echo(response)
    except Exception as e:
        click.echo(f"Error fetching Cache details: {e}", err=True)
        raise SystemExit(1)

@caches.command("list-caches")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
def list_caches(base_url, token):
    """List all Caches."""
    from apigee_sdk.caches_client import CachesClient

    client = CachesClient(base_url, token)
    try:
        response = client.list_caches()
        click.echo(response)
    except Exception as e:
        click.echo(f"Error listing Caches: {e}", err=True)
        raise SystemExit(1)

@caches.command("update-cache")
@click.option('--base-url', required=True, help='Base URL of the Apigee Management API.')
@click.option('--token', required=True, help='Authentication token for the API.')
@click.option('--cache-id', required=True, help='Cache ID to update.')
@click.option('--payload', required=True, help='Payload in JSON format.')
def update_cache(base_url, token, cache_id, payload):
    """Update a Cache."""
    from apigee_sdk.caches_client import CachesClient

    client = CachesClient(base_url, token)
    try:
        import json
        response = client.update_cache(cache_id, json.loads(payload))
        click.echo(response)
    except Exception as e:
        click.echo(f"Error updating Cache: {e}", err=True)
        raise SystemExit(1)

# Ensure the user_roles command group is registered with the main CLI group
cli.add_command(user_roles)

if __name__ == '__main__':
    cli()