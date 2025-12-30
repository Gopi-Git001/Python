from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("Key existed in the path file")
else:
    print('No Key found')
    
from openai import OpenAI

openai = OpenAI()

messages = [{'role':"user","content":"Hi"}]

response = openai.chat.completions.content(
    model = "gpt-4o-mini",
    messages = messages
)

answer = response.choices[0].message.content 

print(answer)

