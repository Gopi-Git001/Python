from dotenv import load_dotenv

import os

from openai import OpenAI

openai = OpenAI()

message = [{'role':'user','contents':'Hi'}]

response = openai.chat.completions.create(
    model = 'gpt-4o-mini',
    messages = message
)

question = response.choices[0].message.content 
print(question)
