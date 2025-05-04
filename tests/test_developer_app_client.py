import unittest
from unittest.mock import patch, MagicMock
from apigee_sdk.developer_app_client import DeveloperAppClient

class TestDeveloperAppClient(unittest.TestCase):

    def setUp(self):
        self.client = DeveloperAppClient(base_url="https://api.example.com", token="test-token")

    @patch("requests.post")
    def test_add_api_key(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {"key": "value"}
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        payload = {"name": "test"}
        response = self.client.add_api_key("app-id", payload)

        mock_post.assert_called_once_with(
            "https://api.example.com/apps/app-id/api-keys",
            headers={"Content-Type": "application/json", "Authorization": "Bearer test-token"},
            json=payload
        )
        self.assertEqual(response, {"key": "value"})

    @patch("requests.post")
    def test_approve_api_key(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "approved"}
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        response = self.client.approve_api_key("app-id", "api-key-id")

        mock_post.assert_called_once_with(
            "https://api.example.com/apps/app-id/api-keys/api-key-id/approve",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"status": "approved"})

    @patch("requests.post")
    def test_create_app(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {"app": "created"}
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        payload = {"name": "new-app"}
        response = self.client.create_app(payload)

        mock_post.assert_called_once_with(
            "https://api.example.com/apps",
            headers={"Content-Type": "application/json", "Authorization": "Bearer test-token"},
            json=payload
        )
        self.assertEqual(response, {"app": "created"})

    @patch("requests.delete")
    def test_delete_app(self, mock_delete):
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "deleted"}
        mock_response.status_code = 200
        mock_delete.return_value = mock_response

        response = self.client.delete_app("app-id")

        mock_delete.assert_called_once_with(
            "https://api.example.com/apps/app-id",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"status": "deleted"})

    @patch("requests.get")
    def test_fetch_app_details(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"app": "details"}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = self.client.fetch_app_details("app-id")

        mock_get.assert_called_once_with(
            "https://api.example.com/apps/app-id",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"app": "details"})

    @patch("requests.get")
    def test_list_apps(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"apps": ["app1", "app2"]}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = self.client.list_apps()

        mock_get.assert_called_once_with(
            "https://api.example.com/apps",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"apps": ["app1", "app2"]})

    @patch("requests.post")
    def test_revoke_api_key(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "revoked"}
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        response = self.client.revoke_api_key("app-id", "api-key-id")

        mock_post.assert_called_once_with(
            "https://api.example.com/apps/app-id/api-keys/api-key-id/revoke",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"status": "revoked"})

    @patch("requests.put")
    def test_update_app(self, mock_put):
        mock_response = MagicMock()
        mock_response.json.return_value = {"app": "updated"}
        mock_response.status_code = 200
        mock_put.return_value = mock_response

        payload = {"name": "updated-app"}
        response = self.client.update_app("app-id", payload)

        mock_put.assert_called_once_with(
            "https://api.example.com/apps/app-id",
            headers={"Content-Type": "application/json", "Authorization": "Bearer test-token"},
            json=payload
        )
        self.assertEqual(response, {"app": "updated"})

if __name__ == "__main__":
    unittest.main()