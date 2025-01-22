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
        print(f"API Key for '{username}': {api_key}")
        return api_key
    else:
        print(f"Failed to request API key: {response.status_code}, {response.text}")
        return None
    
def test_protected_route(api_key):
    """Access the protected route using an API key."""
    headers = {"X-API-KEY": api_key}
    response = requests.get(f"{BASE_URL}/protected", headers=headers)
    if response.status_code == 200:
        print("Protected Route Response:", response.json())
    else:
        print(f"Access Denied: {response.status_code}, {response.text}")

def main():
    # Step 1: Request an API key
    username = "test_user"
    api_key = test_request_api_key(username)

    if not api_key:
        return

    # Step 2: Access the protected route
    print("\nTesting with valid API key:")
    test_protected_route(api_key)

    # Step 3: Test with an invalid API key
    print("\nTesting with invalid API key:")
    test_protected_route("invalid_api_key")

if __name__ == "__main__":
    main()