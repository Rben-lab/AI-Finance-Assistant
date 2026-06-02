# Generate smart financial insights
def generate_smart_insights(
    income,
    expenses,
    remaining,
    profile
):

    # Store generated insights
    insights = []

    # Calculate savings percentage
    savings_rate = (
        remaining / income
    ) * 100

    # Analyze savings condition
    if savings_rate >= 30:

        insights.append(
            "✅ Excellent savings rate."
        )

    elif savings_rate >= 15:

        insights.append(
            "⚠️ Moderate savings rate. Consider saving more."
        )

    else:

        insights.append(
            "🚨 Very low savings rate."
        )

    # Calculate expense ratio
    expense_ratio = (
        expenses / income
    ) * 100

    # Analyze spending condition
    if expense_ratio > 80:

        insights.append(
            "🚨 Your expenses are dangerously high."
        )

    elif expense_ratio > 60:

        insights.append(
            "⚠️ Your spending is relatively high."
        )

    else:

        insights.append(
            "✅ Your spending is under control."
        )

    # Generate recommendation based on profile type
    if profile == "Student Investor":

        insights.append(
            "📈 Focus on long-term ETF and stock accumulation."
        )

    elif profile == "Balanced":

        insights.append(
            "⚖️ Maintain balance between investing and saving."
        )

    else:

        insights.append(
            "🛡️ Conservative profile detected. Prioritize financial safety."
        )

    # Return all generated insights
    return insights
