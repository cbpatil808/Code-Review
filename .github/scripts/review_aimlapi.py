import os
import requests

API_KEY = os.getenv("AIMLAPI_API_KEY")
API_URL = "https://api.aimlapi.com/v1/chat/completions"

def get_code_review(diff_text):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a senior software engineer and code reviewer."},
            {"role": "user", "content": f"Review the following code diff and provide summary, suggestions, risks, and test cases:\n{diff_text}"}
        ],
        "temperature": 0.7,
        "max_tokens": 512
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()
    return data['choices'][0]['message']['content']

if __name__ == "__main__":
    with open("diff.txt", "r") as f:
        diff = f.read()
    review = get_code_review(diff)
    print("AI Code Review:\n", review)
