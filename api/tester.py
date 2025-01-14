import requests
print(requests.post(
        "http://127.0.0.1:8000/process",
        json={"input": "i bought a property in egypt"},
        ).json()
    )

print(requests.get("http://127.0.0.1:80000/protected"))