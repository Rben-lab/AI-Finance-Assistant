# Import Gemini AI library
import google.generativeai as genai

# Import OS module for environment variables
import os

# Import dotenv to load .env file
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API key
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Initialize Gemini AI model
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# Generate AI financial advice
def generate_budget_advice(
    income,
    expenses,
    remaining
):

    # Create AI prompt using financial data
    prompt = f"""
    You are an AI financial advisor.

    User profile:
    Student Investor

    Monthly income:
    Rp {income}

    Total expenses:
    Rp {expenses}

    Remaining balance:
    Rp {remaining}

    Give:
    - financial analysis
    - budgeting advice
    - investment suggestion
    - saving recommendation

    Keep response practical and concise.
    """

    # Generate AI response
    response = model.generate_content(prompt)

    # Return generated advice text
    return response.text
