import os
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a code reviewer AI."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    with open("diff.txt", "r") as f:
        diff = f.read()
    print(get_code_review(diff))
