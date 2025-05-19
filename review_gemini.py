import os
import requests
import json

def get_code_review(diff):
    prompt = f"""
You are a senior software engineer. Review the following code changes and provide:
- Summary
- Suggestions for improvement
- Key risks
- Test case considerations

Code Diff:
{diff}
"""

    api_key = os.environ["GEMINI_API_KEY"]
    url = f"https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText?key={api_key}"

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": {
            "text": prompt
        },
        "temperature": 0.2,
        "maxOutputTokens": 500,
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response.raise_for_status()
    result = response.json()

    return result.get("candidates", [{}])[0].get("output", "No response")

if __name__ == "__main__":
    with open("diff.txt", "r") as f:
        diff = f.read()
    review = get_code_review(diff)
    print("\n=== AI Code Review ===\n")
    print(review)
