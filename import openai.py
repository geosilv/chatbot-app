import openai

openai.api_key = "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"
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello, world!"}],
)
print(response["choices"][0]["message"]["content"])
