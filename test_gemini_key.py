import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("No GOOGLE_API_KEY found in environment.")
    exit(1)

try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0.1,
        google_api_key=api_key
    )
    response = llm.invoke("Hello! Can you confirm you are working?")
    print("LLM response:", response)
except Exception as e:
    print("Error communicating with Gemini API:", e)
