import unittest
from unittest.mock import patch, MagicMock
from apigee_sdk.keystores_client import KeystoresClient

class TestKeystoresClient(unittest.TestCase):

    def setUp(self):
        self.client = KeystoresClient(base_url="https://api.example.com", token="test-token")

    @patch("requests.post")
    def test_create_keystore(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {"keystore": "created"}
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        payload = {"name": "new-keystore"}
        response = self.client.create_keystore(payload)

        mock_post.assert_called_once_with(
            "https://api.example.com/keystores",
            headers={"Content-Type": "application/json", "Authorization": "Bearer test-token"},
            json=payload
        )
        self.assertEqual(response, {"keystore": "created"})

    @patch("requests.delete")
    def test_delete_keystore(self, mock_delete):
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "deleted"}
        mock_response.status_code = 200
        mock_delete.return_value = mock_response

        response = self.client.delete_keystore("keystore-id")

        mock_delete.assert_called_once_with(
            "https://api.example.com/keystores/keystore-id",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"status": "deleted"})

    @patch("requests.get")
    def test_fetch_keystore_details(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"keystore": "details"}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = self.client.fetch_keystore_details("keystore-id")

        mock_get.assert_called_once_with(
            "https://api.example.com/keystores/keystore-id",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"keystore": "details"})

    @patch("requests.get")
    def test_list_keystores(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"keystores": ["keystore1", "keystore2"]}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = self.client.list_keystores()

        mock_get.assert_called_once_with(
            "https://api.example.com/keystores",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"keystores": ["keystore1", "keystore2"]})

    @patch("requests.put")
    def test_update_keystore(self, mock_put):
        mock_response = MagicMock()
        mock_response.json.return_value = {"keystore": "updated"}
        mock_response.status_code = 200
        mock_put.return_value = mock_response

        payload = {"name": "updated-keystore"}
        response = self.client.update_keystore("keystore-id", payload)

        mock_put.assert_called_once_with(
            "https://api.example.com/keystores/keystore-id",
            headers={"Content-Type": "application/json", "Authorization": "Bearer test-token"},
            json=payload
        )
        self.assertEqual(response, {"keystore": "updated"})

if __name__ == "__main__":
    unittest.main()