import unittest
from unittest.mock import patch, MagicMock
from apigee_sdk.shared_flows_client import SharedFlowsClient

class TestSharedFlowsClient(unittest.TestCase):

    def setUp(self):
        self.client = SharedFlowsClient(base_url="https://api.example.com", token="test-token")

    @patch("requests.post")
    def test_create_shared_flow(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {"sharedFlow": "created"}
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        payload = {"name": "new-shared-flow"}
        response = self.client.create_shared_flow(payload)

        mock_post.assert_called_once_with(
            "https://api.example.com/shared-flows",
            headers={"Content-Type": "application/json", "Authorization": "Bearer test-token"},
            json=payload
        )
        self.assertEqual(response, {"sharedFlow": "created"})

    @patch("requests.delete")
    def test_delete_shared_flow(self, mock_delete):
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "deleted"}
        mock_response.status_code = 200
        mock_delete.return_value = mock_response

        response = self.client.delete_shared_flow("shared-flow-id")

        mock_delete.assert_called_once_with(
            "https://api.example.com/shared-flows/shared-flow-id",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"status": "deleted"})

    @patch("requests.get")
    def test_fetch_shared_flow_details(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"sharedFlow": "details"}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = self.client.fetch_shared_flow_details("shared-flow-id")

        mock_get.assert_called_once_with(
            "https://api.example.com/shared-flows/shared-flow-id",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"sharedFlow": "details"})

    @patch("requests.get")
    def test_list_shared_flows(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"sharedFlows": ["sharedFlow1", "sharedFlow2"]}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = self.client.list_shared_flows()

        mock_get.assert_called_once_with(
            "https://api.example.com/shared-flows",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"sharedFlows": ["sharedFlow1", "sharedFlow2"]})

    @patch("requests.put")
    def test_update_shared_flow(self, mock_put):
        mock_response = MagicMock()
        mock_response.json.return_value = {"sharedFlow": "updated"}
        mock_response.status_code = 200
        mock_put.return_value = mock_response

        payload = {"name": "updated-shared-flow"}
        response = self.client.update_shared_flow("shared-flow-id", payload)

        mock_put.assert_called_once_with(
            "https://api.example.com/shared-flows/shared-flow-id",
            headers={"Content-Type": "application/json", "Authorization": "Bearer test-token"},
            json=payload
        )
        self.assertEqual(response, {"sharedFlow": "updated"})

if __name__ == "__main__":
    unittest.main()