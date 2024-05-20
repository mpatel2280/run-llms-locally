import ollama

response = ollama.generate(model='gemma:2b',
prompt='what is a ollama?')
print(response['response'])
