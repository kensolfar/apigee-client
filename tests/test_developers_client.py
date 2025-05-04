import unittest
from unittest.mock import patch, MagicMock
from apigee_sdk.developers_client import DevelopersClient

class TestDevelopersClient(unittest.TestCase):

    def setUp(self):
        self.client = DevelopersClient(base_url="https://api.example.com", token="test-token")

    @patch("requests.post")
    def test_create_developer(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {"developer": "created"}
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        payload = {"email": "new-developer@example.com"}
        response = self.client.create_developer(payload)

        mock_post.assert_called_once_with(
            "https://api.example.com/developers",
            headers={"Content-Type": "application/json", "Authorization": "Bearer test-token"},
            json=payload
        )
        self.assertEqual(response, {"developer": "created"})

    @patch("requests.delete")
    def test_delete_developer(self, mock_delete):
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "deleted"}
        mock_response.status_code = 200
        mock_delete.return_value = mock_response

        response = self.client.delete_developer("developer-id")

        mock_delete.assert_called_once_with(
            "https://api.example.com/developers/developer-id",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"status": "deleted"})

    @patch("requests.get")
    def test_fetch_developer_details(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"developer": "details"}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = self.client.fetch_developer_details("developer-id")

        mock_get.assert_called_once_with(
            "https://api.example.com/developers/developer-id",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"developer": "details"})

    @patch("requests.get")
    def test_list_developers(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"developers": ["developer1", "developer2"]}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = self.client.list_developers()

        mock_get.assert_called_once_with(
            "https://api.example.com/developers",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"developers": ["developer1", "developer2"]})

    @patch("requests.put")
    def test_update_developer(self, mock_put):
        mock_response = MagicMock()
        mock_response.json.return_value = {"developer": "updated"}
        mock_response.status_code = 200
        mock_put.return_value = mock_response

        payload = {"email": "updated-developer@example.com"}
        response = self.client.update_developer("developer-id", payload)

        mock_put.assert_called_once_with(
            "https://api.example.com/developers/developer-id",
            headers={"Content-Type": "application/json", "Authorization": "Bearer test-token"},
            json=payload
        )
        self.assertEqual(response, {"developer": "updated"})

if __name__ == "__main__":
    unittest.main()