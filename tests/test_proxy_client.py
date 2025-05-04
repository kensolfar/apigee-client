import pytest
from apigee_sdk.proxy_client import ProxyClient

def test_create_api_proxy(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "API Proxy created successfully"}
    mocker.patch("requests.post", return_value=mock_response)

    client = ProxyClient("https://api.enterprise.apigee.com", "test_token")
    payload = {"name": "test-proxy"}
    response = client.create_api_proxy("test_org", payload, "test_token")

    assert response["message"] == "API Proxy created successfully"

def test_upload_proxy_revision(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "Revision uploaded successfully"}
    mocker.patch("requests.post", return_value=mock_response)

    client = ProxyClient("https://api.enterprise.apigee.com", "test_token")
    payload = {"revision": "1"}
    response = client.upload_proxy_revision("test_org", "test_api", payload, "test_token")

    assert response["message"] == "Revision uploaded successfully"

def test_list_proxy_revisions(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = ["1", "2", "3"]
    mocker.patch("requests.get", return_value=mock_response)

    client = ProxyClient("https://api.enterprise.apigee.com", "test_token")
    response = client.list_proxy_revisions("test_org", "test_api", "test_token")

    assert response == ["1", "2", "3"]

def test_deploy_proxy_revision(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "Revision deployed successfully"}
    mocker.patch("requests.post", return_value=mock_response)

    client = ProxyClient("https://api.enterprise.apigee.com", "test_token")
    response = client.deploy_proxy_revision("test_org", "test_env", "test_api", "1", "test_token")

    assert response["message"] == "Revision deployed successfully"

def test_get_deployment_status(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"status": "deployed"}
    mocker.patch("requests.get", return_value=mock_response)

    client = ProxyClient("https://api.enterprise.apigee.com", "test_token")
    response = client.get_deployment_status("test_org", "test_env", "test_api", "test_token")

    assert response["status"] == "deployed"

def test_delete_deployment(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "Deployment deleted successfully"}
    mocker.patch("requests.delete", return_value=mock_response)

    client = ProxyClient("https://api.enterprise.apigee.com", "test_token")
    response = client.delete_deployment("test_org", "test_env", "test_api", "1", "test_token")

    assert response["message"] == "Deployment deleted successfully"

def test_update_proxy_policies(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "Policies updated successfully"}
    mocker.patch("requests.put", return_value=mock_response)

    client = ProxyClient("https://api.enterprise.apigee.com", "test_token")
    payload = {"policy": "example-policy"}
    response = client.update_proxy_policies("test_org", "test_api", "1", payload, "test_token")

    assert response["message"] == "Policies updated successfully"

def test_get_proxy_revision_details(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"revision": "1"}
    mocker.patch("requests.get", return_value=mock_response)

    client = ProxyClient("https://api.enterprise.apigee.com", "test_token")
    response = client.get_proxy_revision_details("test_org", "test_api", "1", "test_token")

    assert response["revision"] == "1"

def test_list_apis(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = ["api1", "api2"]
    mocker.patch("requests.get", return_value=mock_response)

    client = ProxyClient("https://api.enterprise.apigee.com", "test_token")
    response = client.list_apis("test_org", "test_token")

    assert response == ["api1", "api2"]

def test_delete_api(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "API deleted successfully"}
    mocker.patch("requests.delete", return_value=mock_response)

    client = ProxyClient("https://api.enterprise.apigee.com", "test_token")
    response = client.delete_api("test_org", "test_api", "test_token")

    assert response["message"] == "API deleted successfully"

def test_start_debug_session(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"session": "debug-session-id"}
    mocker.patch("requests.post", return_value=mock_response)

    client = ProxyClient("https://api.enterprise.apigee.com", "test_token")
    response = client.start_debug_session("test_org", "test_env", "test_api", "1", "test_token")

    assert response["session"] == "debug-session-id"

def test_get_api_metrics(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"metrics": "example-metrics"}
    mocker.patch("requests.get", return_value=mock_response)

    client = ProxyClient("https://api.enterprise.apigee.com", "test_token")
    response = client.get_api_metrics("test_org", "test_env", "test_token")

    assert response["metrics"] == "example-metrics"

def test_create_api_product(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "API product created successfully"}
    mocker.patch("requests.post", return_value=mock_response)

    client = ProxyClient("https://api.enterprise.apigee.com", "test_token")
    payload = {"name": "example-product"}
    response = client.create_api_product("test_org", payload, "test_token")

    assert response["message"] == "API product created successfully"

def test_update_api_product(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "API product updated successfully"}
    mocker.patch("requests.put", return_value=mock_response)

    client = ProxyClient("https://api.enterprise.apigee.com", "test_token")
    payload = {"name": "updated-product"}
    response = client.update_api_product("test_org", "example-product", payload, "test_token")

    assert response["message"] == "API product updated successfully"

def test_promote_revision_to_production(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "Revision promoted to production successfully"}
    mocker.patch("requests.post", return_value=mock_response)

    client = ProxyClient("https://api.enterprise.apigee.com", "test_token")
    response = client.promote_revision_to_production("test_org", "test_api", "1", "test_token")

    assert response["message"] == "Revision promoted to production successfully"

def test_delete_proxy_revision(mocker):
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"message": "Proxy revision deleted successfully"}
    mocker.patch("requests.delete", return_value=mock_response)

    client = ProxyClient("https://api.enterprise.apigee.com", "test_token")
    response = client.delete_proxy_revision("test_org", "test_api", "1", "test_token")

    assert response["message"] == "Proxy revision deleted successfully"