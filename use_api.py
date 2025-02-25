import requests
import json


def getData():
    url = "http://localhost:11434/api/generate"

    data = {
        "model": "llama3.2",
        "prompt": "tell me a short story in 4 lines and make it funny"
    }

    response = requests.post(url, json=data, stream=True)
    if response.status_code == 200:
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode("utf-8")
                result = json.loads(decoded_line)
                generated_text = result.get("response", "")
                print(generated_text, end="", flush=True)
    else:
        print("Error:", response.status_code, response.text)


getData()
