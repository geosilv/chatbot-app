from openai import OpenAI

# Initialize the client with your API key
client = OpenAI(api_key="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")

# Make a chat completion request
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, world!"}
    ]
)

# Print the assistant's reply
print(response.choices[0].message.content)