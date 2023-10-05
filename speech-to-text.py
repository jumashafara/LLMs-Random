import requests

API_URL = "https://api-inference.huggingface.co/models/codenamewei/speech-to-text"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("whats.mpeg")

print(output)