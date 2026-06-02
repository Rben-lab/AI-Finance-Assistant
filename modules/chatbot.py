# Import Gemini AI library
import google.generativeai as genai

# Import OS module for environment variables
import os

# Import dotenv to load .env configuration
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure Gemini API key
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Initialize Gemini AI model
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# Financial chatbot function
def financial_chatbot(user_message, profile):

    # Create AI prompt with user profile and question
    prompt = f"""
    You are an AI financial assistant.

    User financial profile:
    {profile}

    User question:
    {user_message}

    Give practical financial advice.
    Keep answers concise and beginner friendly.
    """

    # Generate AI response
    response = model.generate_content(prompt)

    # Return chatbot response text
    return response.text
