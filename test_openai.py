from openai import OpenAI

client = OpenAI()
# client = OpenAI(api_key="sk-NEWKEYHERE")
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say hello in one sentence"}]
)

print(response.choices[0].message.content)
