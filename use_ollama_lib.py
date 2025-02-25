import ollama


def call_me():
    response = ollama.list()
    res = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "user", "content": "tell me a joke about Harry potter - easy to understand"}
        ])
    print(res["message"]["content"])


call_me()
