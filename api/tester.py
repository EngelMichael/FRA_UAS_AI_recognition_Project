import requests

BASE_URL = "http://127.0.0.1:8000"


def test_request_api_key(username):
    """Request a new API key for a given username."""
    response = requests.post(
        f"{BASE_URL}/request-api-key",
        json={"username": username}
    )
    if response.status_code == 200:
        api_key = response.json().get("api_key")
        print(f"API Key loaded:'{username}'")
        return api_key
    
    else:
        print(f"Failed to request API key: {response.status_code}, {response.text}")
        return None
    
def test_protected_route(input_text, api_key):
    """Access the protected route using an API key."""
    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }
    data = {"input": input_text}
    response = requests.post(f"{BASE_URL}/process", json=data, headers=headers)

    if response.status_code == 200:
        print("Process Response:", response.json())
    else:
        print(f"Access Denied: {response.status_code}, {response.text}")
