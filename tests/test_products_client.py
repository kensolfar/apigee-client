import unittest
from unittest.mock import patch, MagicMock
from apigee_sdk.products_client import ProductsClient

class TestProductsClient(unittest.TestCase):

    def setUp(self):
        self.client = ProductsClient(base_url="https://api.example.com", token="test-token")

    @patch("requests.post")
    def test_create_product(self, mock_post):
        mock_response = MagicMock()
        mock_response.json.return_value = {"product": "created"}
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        payload = {"name": "new-product"}
        response = self.client.create_product(payload)

        mock_post.assert_called_once_with(
            "https://api.example.com/products",
            headers={"Content-Type": "application/json", "Authorization": "Bearer test-token"},
            json=payload
        )
        self.assertEqual(response, {"product": "created"})

    @patch("requests.delete")
    def test_delete_product(self, mock_delete):
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "deleted"}
        mock_response.status_code = 200
        mock_delete.return_value = mock_response

        response = self.client.delete_product("product-id")

        mock_delete.assert_called_once_with(
            "https://api.example.com/products/product-id",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"status": "deleted"})

    @patch("requests.get")
    def test_fetch_product_details(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"product": "details"}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = self.client.fetch_product_details("product-id")

        mock_get.assert_called_once_with(
            "https://api.example.com/products/product-id",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"product": "details"})

    @patch("requests.get")
    def test_list_products(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"products": ["product1", "product2"]}
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = self.client.list_products()

        mock_get.assert_called_once_with(
            "https://api.example.com/products",
            headers={"Authorization": "Bearer test-token"}
        )
        self.assertEqual(response, {"products": ["product1", "product2"]})

    @patch("requests.put")
    def test_update_product(self, mock_put):
        mock_response = MagicMock()
        mock_response.json.return_value = {"product": "updated"}
        mock_response.status_code = 200
        mock_put.return_value = mock_response

        payload = {"name": "updated-product"}
        response = self.client.update_product("product-id", payload)

        mock_put.assert_called_once_with(
            "https://api.example.com/products/product-id",
            headers={"Content-Type": "application/json", "Authorization": "Bearer test-token"},
            json=payload
        )
        self.assertEqual(response, {"product": "updated"})

if __name__ == "__main__":
    unittest.main()