import requests

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-xxl"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "Who is juma shafara",
})
print(output)