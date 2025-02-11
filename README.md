## FRA_UAS_AI_recognition_Project

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.10.2%2B-blue)
![Build](https://img.shields.io/badge/build-passing-brightgreen)

A simple Text Classifier API based on the RoBERTa model.

---

## Installation

1. **Clone the Repository:**
  ```bash
  git clone https://github.com/EngelMichael/FRA_UAS_AI_recognition_Project.git
  cd FRA_UAS_AI_recognition_Project
  ```

2. **Create a Virtual Environment:**
  ```bash
  python -m venv venv
  source venv/bin/activate  # Linux/macOS
  # OR
  venv\Scripts\activate     # Windows
  ```

3. **Install Dependencies:**
  ```bash
  pip install -r requirements.txt
  ```

4. **(Optional) Import roberta_model into the directory:**
  ```bash
  ├── roberta_model
  │   ├── config.json
  │   ├── merges.txt
  │   ├── model.safetensors
  │   ├── special_tokens_map.json
  │   ├── tokenizer.json
  │   ├── tokenizer_config.json
  │   └── vocab.json
  ...
  ```

5. **Run the API Server:**
  ```bash
  uvicorn main:app --reload
  ```
---

## Usage

### Example Request:

```bash
curl -X POST "http://localhost:8000/request-api-key" \
     -H "Content-Type: application/json" \
     -d '{"username": "User 1"}'
```

```bash
curl -X POST "http://localhost:8000/process" \
     -H "X-API-KEY: your_api_key_here" \
     -H "Content-Type: application/json" \
     -d '{"input": "This is a sample text to classify."}'
```
For convenience, we have created tester files which can be used for the request.
1. **Specify server ip and port in tester.py:**
  ```bash
  SERVER_IP = "http://127.0.0.1"
  PORT = "8000"
  ```
2. **Run tui.py with Python and choose a username:**
  ```bash
  python tui.py
  ```
  ```bash
  Welcome to the Tester Program of the FRA_UAS_AI_recognition_Project!
  Please choose an username:
  ```
  >Upon choosing a username, a key request will be sent to the API. If the request fails, you can try again with 'key'
  
3. **Available Commands:**
  ```bash
  file     #Insert your input text into example.txt
  request  #Insert your input text directly into command line
  key      #Reload key if connection to API is established
  user     #Change your current username and attempt key request
  ```


---

## API Endpoints

| Method | Endpoint             | Description                   | Auth Required |
|--------|----------------------|-------------------------------|---------------|
| POST   | `/request-api-key`   | Request a new API key         |      No       |
| POST   | `/process`           | Classify text input           |      Yes      |

---

## License

This project is licensed under the [MIT License](LICENSE).

---
