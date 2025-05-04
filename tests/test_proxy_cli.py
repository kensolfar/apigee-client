import unittest
from unittest.mock import patch
from click.testing import CliRunner
from cli import cli

class TestProxyCLI(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def test_proxy_action_invalid(self):
        result = self.runner.invoke(cli, ['proxy', 'invalid_action', '--base-url', 'https://api.example.com', '--token', 'test-token'])
        self.assertEqual(result.exit_code, 2)
        self.assertIn("Error: No such command 'invalid_action'.", result.output)

    def test_app_action_invalid(self):
        result = self.runner.invoke(cli, ['app', 'invalid_action', '--base-url', 'https://api.example.com', '--token', 'test-token'])
        self.assertEqual(result.exit_code, 2)
        self.assertIn("Error: No such command 'invalid_action'.", result.output)

    def test_kvm_action_invalid(self):
        result = self.runner.invoke(cli, ['kvm', 'invalid_action', '--base-url', 'https://api.example.com', '--token', 'test-token'])
        self.assertEqual(result.exit_code, 2)
        self.assertIn("Error: No such command 'invalid_action'.", result.output)

    def test_proxy_action_missing_argument(self):
        result = self.runner.invoke(cli, ['proxy', 'list_proxy_revisions', '--base-url', 'https://api.example.com'])
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("Error: No such command 'list_proxy_revisions'.", result.output)

    @patch("apigee_sdk.kvm_client.KVMClient.list_kvms")
    def test_kvm_action_success(self, mock_list_kvms):
        mock_list_kvms.return_value = {"kvms": ["kvm1", "kvm2"]}

        result = self.runner.invoke(cli, ['kvm', 'list-kvms', '--base-url', 'https://api.example.com', '--token', 'test-token'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("kvm1", result.output)
        self.assertIn("kvm2", result.output)

    @patch("apigee_sdk.developer_app_client.DeveloperAppClient.create_app")
    def test_app_create_success(self, mock_create_app):
        mock_create_app.return_value = {"app": "created"}

        result = self.runner.invoke(cli, ['app', 'create-app', '--base-url', 'https://api.example.com', '--token', 'test-token', '--payload', '{"name": "new-app"}'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("created", result.output)

    @patch("apigee_sdk.proxy_client.ProxyClient.create_api_proxy")
    def test_proxy_create_success(self, mock_create_api_proxy):
        mock_create_api_proxy.return_value = {"message": "API Proxy created successfully"}

        result = self.runner.invoke(cli, ['proxy', 'create-api-proxy', '--base-url', 'https://api.example.com', '--token', 'test-token', '--org', 'test-org', '--payload', '{"name": "test-proxy"}'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("API Proxy created successfully", result.output)

    @patch("apigee_sdk.kvm_client.KVMClient.create_kvm")
    def test_create_kvm(self, mock_create_kvm):
        mock_create_kvm.return_value = {"kvm": "created"}

        result = self.runner.invoke(cli, ['kvm', 'create-kvm', '--base-url', 'https://api.example.com', '--token', 'test-token', '--payload', '{"name": "new-kvm"}'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("created", result.output)

    @patch("apigee_sdk.kvm_client.KVMClient.delete_kvm")
    def test_delete_kvm(self, mock_delete_kvm):
        mock_delete_kvm.return_value = {"status": "deleted"}

        result = self.runner.invoke(cli, ['kvm', 'delete-kvm', '--base-url', 'https://api.example.com', '--token', 'test-token', '--kvm-id', 'kvm-id'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("deleted", result.output)

    @patch("apigee_sdk.kvm_client.KVMClient.fetch_kvm_details")
    def test_fetch_kvm_details(self, mock_fetch_kvm_details):
        mock_fetch_kvm_details.return_value = {"kvm": "details"}

        result = self.runner.invoke(cli, ['kvm', 'fetch-kvm-details', '--base-url', 'https://api.example.com', '--token', 'test-token', '--kvm-id', 'kvm-id'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("details", result.output)

    @patch("apigee_sdk.kvm_client.KVMClient.update_kvm")
    def test_update_kvm(self, mock_update_kvm):
        mock_update_kvm.return_value = {"kvm": "updated"}

        result = self.runner.invoke(cli, ['kvm', 'update-kvm', '--base-url', 'https://api.example.com', '--token', 'test-token', '--kvm-id', 'kvm-id', '--payload', '{"name": "updated-kvm"}'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("updated", result.output)

    @patch("apigee_sdk.developers_client.DevelopersClient.create_developer")
    def test_create_developer(self, mock_create_developer):
        mock_create_developer.return_value = {"developer": "created"}

        result = self.runner.invoke(cli, ['developers', 'create-developer', '--base-url', 'https://api.example.com', '--token', 'test-token', '--payload', '{"email": "new-developer@example.com"}'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("created", result.output)

    @patch("apigee_sdk.developers_client.DevelopersClient.delete_developer")
    def test_delete_developer(self, mock_delete_developer):
        mock_delete_developer.return_value = {"status": "deleted"}

        result = self.runner.invoke(cli, ['developers', 'delete-developer', '--base-url', 'https://api.example.com', '--token', 'test-token', '--developer-id', 'developer-id'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("deleted", result.output)

    @patch("apigee_sdk.developers_client.DevelopersClient.fetch_developer_details")
    def test_fetch_developer_details(self, mock_fetch_developer_details):
        mock_fetch_developer_details.return_value = {"developer": "details"}

        result = self.runner.invoke(cli, ['developers', 'fetch-developer-details', '--base-url', 'https://api.example.com', '--token', 'test-token', '--developer-id', 'developer-id'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("details", result.output)

    @patch("apigee_sdk.developers_client.DevelopersClient.list_developers")
    def test_list_developers(self, mock_list_developers):
        mock_list_developers.return_value = {"developers": ["developer1", "developer2"]}

        result = self.runner.invoke(cli, ['developers', 'list-developers', '--base-url', 'https://api.example.com', '--token', 'test-token'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("developer1", result.output)
        self.assertIn("developer2", result.output)

    @patch("apigee_sdk.developers_client.DevelopersClient.update_developer")
    def test_update_developer(self, mock_update_developer):
        mock_update_developer.return_value = {"developer": "updated"}

        result = self.runner.invoke(cli, ['developers', 'update-developer', '--base-url', 'https://api.example.com', '--token', 'test-token', '--developer-id', 'developer-id', '--payload', '{"email": "updated-developer@example.com"}'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("updated", result.output)

    @patch("apigee_sdk.users_client.UsersClient.create_user")
    def test_create_user(self, mock_create_user):
        mock_create_user.return_value = {"user": "created"}

        result = self.runner.invoke(cli, ['users', 'create-user', '--base-url', 'https://api.example.com', '--token', 'test-token', '--payload', '{"username": "new-user"}'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("created", result.output)

    @patch("apigee_sdk.users_client.UsersClient.delete_user")
    def test_delete_user(self, mock_delete_user):
        mock_delete_user.return_value = {"status": "deleted"}

        result = self.runner.invoke(cli, ['users', 'delete-user', '--base-url', 'https://api.example.com', '--token', 'test-token', '--user-id', 'user-id'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("deleted", result.output)

    @patch("apigee_sdk.users_client.UsersClient.fetch_user_details")
    def test_fetch_user_details(self, mock_fetch_user_details):
        mock_fetch_user_details.return_value = {"user": "details"}

        result = self.runner.invoke(cli, ['users', 'fetch-user-details', '--base-url', 'https://api.example.com', '--token', 'test-token', '--user-id', 'user-id'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("details", result.output)

    @patch("apigee_sdk.users_client.UsersClient.list_users")
    def test_list_users(self, mock_list_users):
        mock_list_users.return_value = {"users": ["user1", "user2"]}

        result = self.runner.invoke(cli, ['users', 'list-users', '--base-url', 'https://api.example.com', '--token', 'test-token'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("user1", result.output)
        self.assertIn("user2", result.output)

    @patch("apigee_sdk.users_client.UsersClient.update_user")
    def test_update_user(self, mock_update_user):
        mock_update_user.return_value = {"user": "updated"}

        result = self.runner.invoke(cli, ['users', 'update-user', '--base-url', 'https://api.example.com', '--token', 'test-token', '--user-id', 'user-id', '--payload', '{"username": "updated-user"}'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("updated", result.output)

    @patch("apigee_sdk.user_roles_client.UserRolesClient.create_user_role")
    def test_create_user_role(self, mock_create_user_role):
        mock_create_user_role.return_value = {"userRole": "created"}

        result = self.runner.invoke(cli, ['user-roles', 'create-user-role', '--base-url', 'https://api.example.com', '--token', 'test-token', '--payload', '{"roleName": "new-role"}'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("created", result.output)

    @patch("apigee_sdk.user_roles_client.UserRolesClient.delete_user_role")
    def test_delete_user_role(self, mock_delete_user_role):
        mock_delete_user_role.return_value = {"status": "deleted"}

        result = self.runner.invoke(cli, ['user-roles', 'delete-user-role', '--base-url', 'https://api.example.com', '--token', 'test-token', '--role-id', 'role-id'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("deleted", result.output)

    @patch("apigee_sdk.user_roles_client.UserRolesClient.fetch_user_role_details")
    def test_fetch_user_role_details(self, mock_fetch_user_role_details):
        mock_fetch_user_role_details.return_value = {"userRole": "details"}

        result = self.runner.invoke(cli, ['user-roles', 'fetch-user-role-details', '--base-url', 'https://api.example.com', '--token', 'test-token', '--role-id', 'role-id'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("details", result.output)

    @patch("apigee_sdk.user_roles_client.UserRolesClient.list_user_roles")
    def test_list_user_roles(self, mock_list_user_roles):
        mock_list_user_roles.return_value = {"userRoles": ["role1", "role2"]}

        result = self.runner.invoke(cli, ['user-roles', 'list-user-roles', '--base-url', 'https://api.example.com', '--token', 'test-token'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("role1", result.output)
        self.assertIn("role2", result.output)

    @patch("apigee_sdk.user_roles_client.UserRolesClient.update_user_role")
    def test_update_user_role(self, mock_update_user_role):
        mock_update_user_role.return_value = {"userRole": "updated"}

        result = self.runner.invoke(cli, ['user-roles', 'update-user-role', '--base-url', 'https://api.example.com', '--token', 'test-token', '--role-id', 'role-id', '--payload', '{"roleName": "updated-role"}'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("updated", result.output)

    @patch("apigee_sdk.keystores_client.KeystoresClient.create_keystore")
    def test_create_keystore(self, mock_create_keystore):
        mock_create_keystore.return_value = {"keystore": "created"}

        result = self.runner.invoke(cli, ['keystores', 'create-keystore', '--base-url', 'https://api.example.com', '--token', 'test-token', '--payload', '{"name": "new-keystore"}'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("created", result.output)

    @patch("apigee_sdk.keystores_client.KeystoresClient.delete_keystore")
    def test_delete_keystore(self, mock_delete_keystore):
        mock_delete_keystore.return_value = {"status": "deleted"}

        result = self.runner.invoke(cli, ['keystores', 'delete-keystore', '--base-url', 'https://api.example.com', '--token', 'test-token', '--keystore-id', 'keystore-id'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("deleted", result.output)

    @patch("apigee_sdk.keystores_client.KeystoresClient.fetch_keystore_details")
    def test_fetch_keystore_details(self, mock_fetch_keystore_details):
        mock_fetch_keystore_details.return_value = {"keystore": "details"}

        result = self.runner.invoke(cli, ['keystores', 'fetch-keystore-details', '--base-url', 'https://api.example.com', '--token', 'test-token', '--keystore-id', 'keystore-id'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("details", result.output)

    @patch("apigee_sdk.keystores_client.KeystoresClient.list_keystores")
    def test_list_keystores(self, mock_list_keystores):
        mock_list_keystores.return_value = {"keystores": ["keystore1", "keystore2"]}

        result = self.runner.invoke(cli, ['keystores', 'list-keystores', '--base-url', 'https://api.example.com', '--token', 'test-token'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("keystore1", result.output)
        self.assertIn("keystore2", result.output)

    @patch("apigee_sdk.keystores_client.KeystoresClient.update_keystore")
    def test_update_keystore(self, mock_update_keystore):
        mock_update_keystore.return_value = {"keystore": "updated"}

        result = self.runner.invoke(cli, ['keystores', 'update-keystore', '--base-url', 'https://api.example.com', '--token', 'test-token', '--keystore-id', 'keystore-id', '--payload', '{"name": "updated-keystore"}'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("updated", result.output)

    @patch("apigee_sdk.caches_client.CachesClient.create_cache")
    def test_create_cache(self, mock_create_cache):
        mock_create_cache.return_value = {"cache": "created"}

        result = self.runner.invoke(cli, ['caches', 'create-cache', '--base-url', 'https://api.example.com', '--token', 'test-token', '--payload', '{"name": "new-cache"}'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("created", result.output)

    @patch("apigee_sdk.caches_client.CachesClient.delete_cache")
    def test_delete_cache(self, mock_delete_cache):
        mock_delete_cache.return_value = {"status": "deleted"}

        result = self.runner.invoke(cli, ['caches', 'delete-cache', '--base-url', 'https://api.example.com', '--token', 'test-token', '--cache-id', 'cache-id'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("deleted", result.output)

    @patch("apigee_sdk.caches_client.CachesClient.fetch_cache_details")
    def test_fetch_cache_details(self, mock_fetch_cache_details):
        mock_fetch_cache_details.return_value = {"cache": "details"}

        result = self.runner.invoke(cli, ['caches', 'fetch-cache-details', '--base-url', 'https://api.example.com', '--token', 'test-token', '--cache-id', 'cache-id'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("details", result.output)

    @patch("apigee_sdk.caches_client.CachesClient.list_caches")
    def test_list_caches(self, mock_list_caches):
        mock_list_caches.return_value = {"caches": ["cache1", "cache2"]}

        result = self.runner.invoke(cli, ['caches', 'list-caches', '--base-url', 'https://api.example.com', '--token', 'test-token'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("cache1", result.output)
        self.assertIn("cache2", result.output)

    @patch("apigee_sdk.caches_client.CachesClient.update_cache")
    def test_update_cache(self, mock_update_cache):
        mock_update_cache.return_value = {"cache": "updated"}

        result = self.runner.invoke(cli, ['caches', 'update-cache', '--base-url', 'https://api.example.com', '--token', 'test-token', '--cache-id', 'cache-id', '--payload', '{"name": "updated-cache"}'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("updated", result.output)

    def test_user_roles_command_group(self):
        result = self.runner.invoke(cli, ['user-roles', '--help'])
        self.assertEqual(result.exit_code, 0, msg=f"Output: {result.output}")
        self.assertIn("Commands:", result.output)
        self.assertIn("create-user-role", result.output)
        self.assertIn("delete-user-role", result.output)
        self.assertIn("fetch-user-role-details", result.output)
        self.assertIn("list-user-roles", result.output)
        self.assertIn("update-user-role", result.output)

if __name__ == "__main__":
    unittest.main()