import requests

# This is the code for simplifying requests to test the API
# For local testing use http://127.0.0.1:8000
# For Livedemo specify IPv4 address of server machine

SERVER_ADDRESS = "127.0.0.1"
PORT = "8000"

#Request to /request-api-key with a given username
def request_api_key(username):
    response = requests.post(
        f"http://{SERVER_ADDRESS}:{PORT}/request-api-key",
        json={"username": username}
    )
    if response.status_code == 200:
        api_key = response.json().get("api_key")
        print(f"API Key loaded:'{username}'")
        return api_key
    
    else:
        print(f"Failed to request API key: {response.status_code}, {response.text}")
        return None
    
#Request to /process with input_text and api_key
def process_data(input_text, api_key):
    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }
    data = {"input": input_text}
    response = requests.post(f"http://{SERVER_ADDRESS}:{PORT}/process", json=data, headers=headers)

    if response.status_code == 200:

        result = response.json()

        # Print the classification and probabilities
        print("\n------------------------------Evaluation------------------------------")
        print(f"The sentence is classified as: {result['classification']}")
        print("Probabilities:")
        for label, prob in result['probabilities'].items():
            print(f"    {label}:    {prob:.4f}")

    else:
        print(f"Access Denied: {response.status_code}, {response.text}")
