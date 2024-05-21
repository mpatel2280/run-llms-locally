from langchain_community.llms import Ollama

llm = Ollama(model="gemma:2b")

llm.invoke("tell me about partial functions in python")
