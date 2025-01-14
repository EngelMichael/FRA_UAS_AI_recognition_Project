from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.security import APIKeyHeader
from pydantic import BaseModel
from typing import List
import secrets

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

# Simulate a database of valid API keys
VALID_API_KEYS = ["your-api-key-here", "another-api-key"]

# APIKeyHeader is used to define where the API key will be passed (in this case, headers)
api_key_header = APIKeyHeader(name="X-API-KEY")

# Dependency to check API key
def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key not in VALID_API_KEYS:
        raise HTTPException(status_code=403, detail="Invalid or missing API key")
    return api_key

class Token(BaseModel):
    access_token: str
    token_type: str

class InputData(BaseModel):
    input: str

@app.post("/")
def root():
    return {"message": "this is the root"}

@app.post("/process")
def process_input(data: InputData):
    data.input

    output_value = f"Processed: {data.input}"
    return {"output": output_value}

@app.get("/protected")
def protected_endpoint(api_key: str = Depends(get_api_key)):
    return {"message": "This is a protected route!", "api_key": api_key}