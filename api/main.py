from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from typing import List
from inference import classify_text_with_probabilities
import secrets, json

# This is the main code for the AI Classifier API using the FastAPI framework.
#
# Packages needed: fastapi, uvicorn
# After running the programm use: uvicorn main:app --reload
# to run the FastAPI server. It will be accessible under:
# http://127.0.0.1:8000 (http://127.0.0.1:8000/docs)
# 
# Resources
# https://www.youtube.com/watch?v=SORiTsvnU28
# https://timberry.dev/fastapi-with-apikeys

app = FastAPI()

# Database for API-Keys
# The keys are in the format:
# {
#    "API-KEY-1": "user1",
#    "API-KEY-2": "user2",
#    "API-KEY-3": "user3",
# }
# Duplicate keys will be avoided on generate

API_KEYS_FILE = "api_keys.json"

# Helper functions for API key management
# The load_api_keys() function will load all keys from the database and return them in the json format.
# FileNotFoundError -> return empty json
def load_api_keys():
    try:
        with open(API_KEYS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# The save_api_keys(api_keys) function will save all keys from a json object to the database.
def save_api_keys(api_keys):
    with open(API_KEYS_FILE, "w") as file:
        json.dump(api_keys, file, indent=4)

# The generate_api_key(username: str) function will generate a key for the given username, save it in the database and return it as a string.
# If the given user already has an entry in the database, the key will be copied from the database
def generate_api_key(username: str) -> str:
    api_keys = load_api_keys()

    # Check if the username already exists
    for api_key, existing_username in api_keys.items():
        if existing_username == username:
            return api_key

    # API-Keys are generated with the secrets library
    api_key = secrets.token_hex(32)
    api_keys[api_key] = username
    save_api_keys(api_keys)
    return api_key

# Dependency to verify API key
api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=False)

def verify_api_key(api_key: str = Depends(api_key_header)):
    api_keys = load_api_keys()
    if api_key not in api_keys:
        raise HTTPException(status_code=403, detail="Invalid or missing API key")
    return api_key

class APIKeyRequest(BaseModel):
    username: str

class InputData(BaseModel):
    input: str

# Endpoints
@app.post("/request-api-key")
def request_api_key(request: APIKeyRequest):
    api_key = generate_api_key(request.username)
    return {"api_key": api_key}

@app.post("/process")
def protected_route_process(data: InputData, api_key: str = Depends(verify_api_key)):
    username = load_api_keys()[api_key]
    print(f"Request from: {username} -> input: {data.input}")
    result = classify_text_with_probabilities(data.input)
    return result
