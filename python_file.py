import os

openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key:
    print("Key Identified")
else:
    print('Please make sure it again cause key is not available ')
    