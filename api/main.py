from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from typing import List
import secrets, json

# API using the FastAPI framework
# Packages needed: fastapi, uvicorn
# After running the programm use: uvicorn main:app --reload
# to run the FastAPI server. It will be accessible under:
# http://127.0.0.1:8000 (http://127.0.0.1:8000/docs)
# 
# Resources
# https://www.youtube.com/watch?v=SORiTsvnU28
# https://timberry.dev/fastapi-with-apikeys

app = FastAPI()

API_KEYS_FILE = "api_keys.json"

# Helper functions for API key management
def load_api_keys():
    try:
        with open(API_KEYS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_api_keys(api_keys):
    with open(API_KEYS_FILE, "w") as file:
        json.dump(api_keys, file, indent=4)

def generate_api_key(username: str) -> str:
    api_keys = load_api_keys()

    # Check if the username already exists
    if username in api_keys.values():
        raise HTTPException(
            status_code=400,
            detail="Username already exists. Please use the existing API key."
        )

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

# Load your own trained model and tokenizer
# model_path = "./my_bert_model"
# tokenizer = BertTokenizer.from_pretrained(model_path)
# model = BertForSequenceClassification.from_pretrained(model_path)

class APIKeyRequest(BaseModel):
    username: str

class InputData(BaseModel):
    input: str

# Endpoints
@app.post("/request-api-key")
def request_api_key(request: APIKeyRequest):
    api_key = generate_api_key(request.username)
    return {"api_key": api_key}

@app.get("/protected")
def protected_route(api_key: str = Depends(verify_api_key)):
    username = load_api_keys()[api_key]
    return {"message": f"Welcome, {username}! This is a protected route."}

@app.post("/process")
def process_input(data: InputData):
    output_value = f"Processed: {data.input}"
    # Process data here
    # 1. Tokenize input text
    # 2. Pass tokenized input to model
    # 3. Evaluate Logits
    return {"output": output_value}