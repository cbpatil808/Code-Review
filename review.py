# review.py
import openai
import sys

openai.api_key = "sk-..."  # Only for local testing, we'll override this in Actions

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
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Or "gpt-3.5-turbo" if on free trial
        messages=[
            {"role": "system", "content": "You are a code reviewer AI."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    diff = sys.stdin.read()
    print(get_code_review(diff))
