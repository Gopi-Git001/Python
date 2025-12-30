from dotenv import load_dotenv
import os

load_dotenv()

from openai import OpenAI

openai = OpenAI()

prompt_1 = "Please propose a hard, challenging question to assess someone's IQ. Respond only with the question."

messages = [{'role':"user","content":prompt_1}]

response = openai.chat.completions.content(
    model = "gpt-4o-mini",
    messages = messages
)

question = response.choices[0].message.content 

print(question)


messages = [{'role':'user','content':question}]

response = openai.chat.completions.content(
    model = 'gpt-4o-mini',
    messages = messages
    
)

answer = response.choices[0].message.content 

print(answer)


