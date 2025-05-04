import unittest
from unittest.mock import patch, MagicMock
from apigee_sdk.users_client import UsersClient

class TestUsersClient(unittest.TestCase):

    def setUp(self):
        self.client = UsersClient(base_url="https://api.example.com", token="test-token")

    @patch("requests.post")
    def test_create_user(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {"user": "created"}
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        payload = {"username": "new-user"}
        response = self.client.create_user(payload)

        mock_post.assert_called_once_with(
            "https://api.example.com/users",
            headers={"Content-Type": "application/json", "Authorization": "Bearer test-token"},
            json=payload
        )
        self.assertEqual(response, {"user": "created"})

    @patch("requests.delete")
    def test_delete_user(self, mock_delete):
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "deleted"}
        mock_response.status_code = 200
        mock_delete.return_value = mock_response

        response = self.client.delete_user("user-id")

        mock_delete.assert_called_once_with(
            "https://api.example.com/users/user-id",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"status": "deleted"})

    @patch("requests.get")
    def test_fetch_user_details(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"user": "details"}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = self.client.fetch_user_details("user-id")

        mock_get.assert_called_once_with(
            "https://api.example.com/users/user-id",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"user": "details"})

    @patch("requests.get")
    def test_list_users(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"users": ["user1", "user2"]}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = self.client.list_users()

        mock_get.assert_called_once_with(
            "https://api.example.com/users",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"users": ["user1", "user2"]})

    @patch("requests.put")
    def test_update_user(self, mock_put):
        mock_response = MagicMock()
        mock_response.json.return_value = {"user": "updated"}
        mock_response.status_code = 200
        mock_put.return_value = mock_response

        payload = {"username": "updated-user"}
        response = self.client.update_user("user-id", payload)

        mock_put.assert_called_once_with(
            "https://api.example.com/users/user-id",
            headers={"Content-Type": "application/json", "Authorization": "Bearer test-token"},
            json=payload
        )
        self.assertEqual(response, {"user": "updated"})

if __name__ == "__main__":
    unittest.main()