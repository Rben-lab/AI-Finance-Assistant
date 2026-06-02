import google.generativeai as genai
import os

from dotenv import load_dotenv

# LOAD ENV
load_dotenv()

# GEMINI CONFIG
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# MODEL
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# CHAT FUNCTION
def financial_chatbot(user_message, profile):

    prompt = f"""
    You are an AI financial assistant.

    User financial profile:
    {profile}

    User question:
    {user_message}

    Give practical financial advice.
    Keep answers concise and beginner friendly.
    """

    response = model.generate_content(prompt)

    return response.text