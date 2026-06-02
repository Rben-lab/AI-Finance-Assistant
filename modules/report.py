# Generate downloadable financial report
def generate_financial_report(
    income,
    expenses,
    remaining,
    score,
    profile
):

    # Create initial financial report template
    report = f"""
AI FINANCIAL REPORT
=============================

Financial Profile:
{profile}

Monthly Income:
Rp {income:,.0f}

Total Expenses:
Rp {expenses:,.0f}

Remaining Balance:
Rp {remaining:,.0f}

Financial Health Score:
{score}/100

=============================
FINANCIAL ANALYSIS
=============================

"""

    # Analyze financial condition based on score
    if score >= 80:

        report += """
Excellent financial condition.
Your spending habits are healthy.
Continue maintaining disciplined investing.
"""

    elif score >= 60:

        report += """
Moderate financial condition.
There is still room for improvement.
Try increasing savings and investment consistency.
"""

    else:

        report += """
Financial condition needs improvement.
Your spending level is relatively high.
Focus on reducing unnecessary expenses.
"""

    # Generate recommendation based on financial profile
    report += "\n\n=============================\n"
    report += "PROFILE RECOMMENDATION\n"
    report += "=============================\n"

    if profile == "Student Investor":

        report += """
Focus on long-term ETF accumulation
and disciplined stock investing.
"""

    elif profile == "Balanced":

        report += """
Maintain balance between saving,
investing, and personal spending.
"""

    else:

        report += """
Prioritize financial stability,
cash reserves, and lower-risk planning.
"""

    # Return final report result
    return report
