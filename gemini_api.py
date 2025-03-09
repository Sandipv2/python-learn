from google import genai
from dotenv import load_dotenv
from time import sleep
import os

load_dotenv()

my_api_key = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key = my_api_key)

while True:
    print('-----------------------------')
    user = input("User : ")
    
    if user in 'bye exit':
        print("Gemini : Have a good day!")
        break
    
    response = client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=user,
    )
    
    print(f"Gemini :", flush=True)
    for ch in response.text:
        print(ch, end='', flush=True)
        sleep(0.025)
    