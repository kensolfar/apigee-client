import unittest
from unittest.mock import patch, MagicMock
from apigee_sdk.kvm_client import KVMClient

class TestKVMClient(unittest.TestCase):

    def setUp(self):
        self.client = KVMClient(base_url="https://api.example.com", token="test-token")

    @patch("requests.post")
    def test_create_kvm(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {"kvm": "created"}
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        payload = {"name": "new-kvm"}
        response = self.client.create_kvm(payload)

        mock_post.assert_called_once_with(
            "https://api.example.com/kvms",
            headers={"Content-Type": "application/json", "Authorization": "Bearer test-token"},
            json=payload
        )
        self.assertEqual(response, {"kvm": "created"})

    @patch("requests.delete")
    def test_delete_kvm(self, mock_delete):
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "deleted"}
        mock_response.status_code = 200
        mock_delete.return_value = mock_response

        response = self.client.delete_kvm("kvm-id")

        mock_delete.assert_called_once_with(
            "https://api.example.com/kvms/kvm-id",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"status": "deleted"})

    @patch("requests.get")
    def test_fetch_kvm_details(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"kvm": "details"}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = self.client.fetch_kvm_details("kvm-id")

        mock_get.assert_called_once_with(
            "https://api.example.com/kvms/kvm-id",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"kvm": "details"})

    @patch("requests.get")
    def test_list_kvms(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"kvms": ["kvm1", "kvm2"]}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = self.client.list_kvms()

        mock_get.assert_called_once_with(
            "https://api.example.com/kvms",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"kvms": ["kvm1", "kvm2"]})

    @patch("requests.put")
    def test_update_kvm(self, mock_put):
        mock_response = MagicMock()
        mock_response.json.return_value = {"kvm": "updated"}
        mock_response.status_code = 200
        mock_put.return_value = mock_response

        payload = {"name": "updated-kvm"}
        response = self.client.update_kvm("kvm-id", payload)

        mock_put.assert_called_once_with(
            "https://api.example.com/kvms/kvm-id",
            headers={"Content-Type": "application/json", "Authorization": "Bearer test-token"},
            json=payload
        )
        self.assertEqual(response, {"kvm": "updated"})

if __name__ == "__main__":
    unittest.main()