import unittest
from unittest.mock import patch, MagicMock
from apigee_sdk.user_roles_client import UserRolesClient

class TestUserRolesClient(unittest.TestCase):

    def setUp(self):
        self.client = UserRolesClient(base_url="https://api.example.com", token="test-token")

    @patch("requests.post")
    def test_create_user_role(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {"userRole": "created"}
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        payload = {"roleName": "new-role"}
        response = self.client.create_user_role(payload)

        mock_post.assert_called_once_with(
            "https://api.example.com/user-roles",
            headers={"Content-Type": "application/json", "Authorization": "Bearer test-token"},
            json=payload
        )
        self.assertEqual(response, {"userRole": "created"})

    @patch("requests.delete")
    def test_delete_user_role(self, mock_delete):
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "deleted"}
        mock_response.status_code = 200
        mock_delete.return_value = mock_response

        response = self.client.delete_user_role("role-id")

        mock_delete.assert_called_once_with(
            "https://api.example.com/user-roles/role-id",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"status": "deleted"})

    @patch("requests.get")
    def test_fetch_user_role_details(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"userRole": "details"}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = self.client.fetch_user_role_details("role-id")

        mock_get.assert_called_once_with(
            "https://api.example.com/user-roles/role-id",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"userRole": "details"})

    @patch("requests.get")
    def test_list_user_roles(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"userRoles": ["role1", "role2"]}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = self.client.list_user_roles()

        mock_get.assert_called_once_with(
            "https://api.example.com/user-roles",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"userRoles": ["role1", "role2"]})

    @patch("requests.put")
    def test_update_user_role(self, mock_put):
        mock_response = MagicMock()
        mock_response.json.return_value = {"userRole": "updated"}
        mock_response.status_code = 200
        mock_put.return_value = mock_response

        payload = {"roleName": "updated-role"}
        response = self.client.update_user_role("role-id", payload)

        mock_put.assert_called_once_with(
            "https://api.example.com/user-roles/role-id",
            headers={"Content-Type": "application/json", "Authorization": "Bearer test-token"},
            json=payload
        )
        self.assertEqual(response, {"userRole": "updated"})

if __name__ == "__main__":
    unittest.main()