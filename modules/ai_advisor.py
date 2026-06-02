import google.generativeai as genai
import os

from dotenv import load_dotenv

# LOAD ENV
load_dotenv()

# CONFIGURE API
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# MODEL
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# FUNCTION
def generate_budget_advice(
    income,
    expenses,
    remaining
):

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

    response = model.generate_content(prompt)

    return response.text