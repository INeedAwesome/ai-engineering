import ollama

prompt = "What is the capital of Sweden?"

model = "llama3.2"
response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
print(response['message']['content'])


model = "bonsai-2"
response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
print(response['message']['content'])

model = "nemotron-3.5-bolt"
response = ollama.chat(
    model=model,
    messages=[{'role': 'user', 'content': prompt}],
)
print(response.message.content)

