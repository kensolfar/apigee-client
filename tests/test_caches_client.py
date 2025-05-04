import unittest
from unittest.mock import patch, MagicMock
from apigee_sdk.caches_client import CachesClient

class TestCachesClient(unittest.TestCase):

    def setUp(self):
        self.client = CachesClient(base_url="https://api.example.com", token="test-token")

    @patch("requests.post")
    def test_create_cache(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {"cache": "created"}
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        payload = {"name": "new-cache"}
        response = self.client.create_cache(payload)

        mock_post.assert_called_once_with(
            "https://api.example.com/caches",
            headers={"Content-Type": "application/json", "Authorization": "Bearer test-token"},
            json=payload
        )
        self.assertEqual(response, {"cache": "created"})

    @patch("requests.delete")
    def test_delete_cache(self, mock_delete):
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "deleted"}
        mock_response.status_code = 200
        mock_delete.return_value = mock_response

        response = self.client.delete_cache("cache-id")

        mock_delete.assert_called_once_with(
            "https://api.example.com/caches/cache-id",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"status": "deleted"})

    @patch("requests.get")
    def test_fetch_cache_details(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"cache": "details"}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = self.client.fetch_cache_details("cache-id")

        mock_get.assert_called_once_with(
            "https://api.example.com/caches/cache-id",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"cache": "details"})

    @patch("requests.get")
    def test_list_caches(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"caches": ["cache1", "cache2"]}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = self.client.list_caches()

        mock_get.assert_called_once_with(
            "https://api.example.com/caches",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"caches": ["cache1", "cache2"]})

    @patch("requests.put")
    def test_update_cache(self, mock_put):
        mock_response = MagicMock()
        mock_response.json.return_value = {"cache": "updated"}
        mock_response.status_code = 200
        mock_put.return_value = mock_response

        payload = {"name": "updated-cache"}
        response = self.client.update_cache("cache-id", payload)

        mock_put.assert_called_once_with(
            "https://api.example.com/caches/cache-id",
            headers={"Content-Type": "application/json", "Authorization": "Bearer test-token"},
            json=payload
        )
        self.assertEqual(response, {"cache": "updated"})

if __name__ == "__main__":
    unittest.main()