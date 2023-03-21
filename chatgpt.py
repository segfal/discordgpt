

import openai
from dotenv import load_dotenv
import os



load_dotenv()


openai.api_key = os.getenv("OPENAI_TOKEN")


def message_response(message):
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {
                "role" : "user",
                "content" : message
            }
        ],
    )
    return response["choices"][0]["message"]["content"]


