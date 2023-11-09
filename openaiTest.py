import requests

url = "https://api.openai.com/v1/chat/completions"
api_key = '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'

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant. and you specialize in make Draft of a Document about business in korean."},
        {"role": "user", "content": "I want to make a document about 'how to make a business plan'"}
    ],
    "model": "gpt-3.5-turbo",
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    result = response.json()
    message = result["choices"][0]["message"]["content"]
    print("Assistant:", message)
else:
    print("Error:", response.status_code, response.text)