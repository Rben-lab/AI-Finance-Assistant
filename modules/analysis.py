import pandas as pd

def analyze_expenses(df):

    total_expense = df["Amount"].sum()

    highest_expense = df.loc[
        df["Amount"].idxmax()
    ]

    average_expense = df["Amount"].mean()

    return {
        "total_expense": total_expense,
        "highest_category": highest_expense["Category"],
        "highest_amount": highest_expense["Amount"],
        "average_expense": average_expense
    }