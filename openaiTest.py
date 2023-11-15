# -*- coding: utf-8 -*
import requests

class OpenaiRequest():
  def openaiRequst(self, token, content):
    url = "https://api.openai.com/v1/chat/completions"
    api_key = token

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant. and you specialize in make Document about business in korean based on given content. document consist of index and each chapter's content. each content is long 500+ word. document condition do not contain in document directe. no skip response"},
            {"role": "user", "content": content}
        ],
        "model": "gpt-4-1106-preview",
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        message = result["choices"][0]["message"]["content"]
        return "Assistant:" + message
    else:
        print("Error:", response.status_code, response.text)