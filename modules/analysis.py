# Import pandas library for data analysis
import pandas as pd

# Analyze uploaded expense transaction data
def analyze_expenses(df):

    # Calculate total expenses
    total_expense = df["Amount"].sum()

    # Find transaction with highest expense
    highest_expense = df.loc[
        df["Amount"].idxmax()
    ]

    # Calculate average expense value
    average_expense = df["Amount"].mean()

    # Return expense analysis results
    return {

        # Total spending amount
        "total_expense": total_expense,

        # Category with highest expense
        "highest_category": highest_expense["Category"],

        # Highest expense amount
        "highest_amount": highest_expense["Amount"],

        # Average transaction amount
        "average_expense": average_expense
    }
