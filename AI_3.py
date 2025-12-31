from dotenv import load_dotenv
import os 

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


from openai import OpenAI

openai = OpenAI()


messages = [{'role':'user','content':'Hi! How are you?'}]

