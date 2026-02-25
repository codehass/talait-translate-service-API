import os

import requests
from dotenv import load_dotenv

load_dotenv()


def translate(input_text, language):
    API_URL = f"https://router.huggingface.co/hf-inference/models/Helsinki-NLP/opus-mt-{language}"
    headers = {
        "Authorization": f"Bearer {os.getenv('HF_TOKEN')}",
    }

    response = requests.post(
        API_URL,
        headers=headers,
        json={"inputs": input_text},
    )

    data = response.json()

    if isinstance(data, list) and len(data) > 0:
        return data[0]

    if isinstance(data, dict):
        return data

    return {"error": "Unexpected response format"}


# print(translate("Hello, how are you?", "en-fr"))
