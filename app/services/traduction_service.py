import os
import requests
from dotenv import load_dotenv

load_dotenv()


def translate(input_text, language):

    API_URL = f"https://router.huggingface.co/hf-inference/models/Helsinki-NLP/opus-mt-{language}"
    headers = {
        "Authorization": f"Bearer {os.getenv('HF_TOKEN')}",
    }

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    return query(
        {
            "inputs": input_text,
        }
    )[0]
