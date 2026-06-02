import streamlit as st
import pandas as pd

from modules.budget import calculate_budget
from modules.ai_advisor import generate_budget_advice
from modules.analysis import analyze_expenses
from modules.chatbot import financial_chatbot
from modules.insight import generate_smart_insights
from modules.report import generate_financial_report

# =========================================
# PAGE CONFIG
# =========================================

st.set_page_config(
    page_title="AI Finance Assistant",
    layout="wide"
)

# =========================================
# TITLE
# =========================================

st.title("💰 AI-Powered Personal Finance Assistant")

# =========================================
# INCOME INPUT
# =========================================

st.header("Monthly Income")

income = st.number_input(
    "Enter your monthly income",
    min_value=0,
    step=100000,
    key="income_input"
)

# =========================================
# FINANCIAL PROFILE
# =========================================

profile = st.selectbox(
    "Choose Financial Profile",
    [
        "Student Investor",
        "Balanced",
        "Conservative"
    ],
    key="profile_select"
)

# =========================================
# MAIN APPLICATION
# =========================================

if income > 0:

    # =====================================
    # BUDGET CALCULATION
    # =====================================

    budget = calculate_budget(
        income,
        profile
    )

    st.header("📊 Recommended Budget Allocation")

    columns = st.columns(len(budget))

    for col, (category, amount) in zip(columns, budget.items()):

        with col:

            st.metric(
                category,
                f"Rp {amount:,.0f}"
            )

    st.divider()

    # =====================================
    # EXPENSE INPUT
    # =====================================

    st.header("💸 Expense Input")

    food = st.number_input(
        "Food",
        min_value=0,
        key="food_input"
    )

    transport = st.number_input(
        "Transport",
        min_value=0,
        key="transport_input"
    )

    entertainment = st.number_input(
        "Entertainment",
        min_value=0,
        key="entertainment_input"
    )

    # =====================================
    # EXPENSE CALCULATION
    # =====================================

    total_expense = (
        food +
        transport +
        entertainment
    )

    remaining = income - total_expense

    # =====================================
    # FINANCIAL SUMMARY
    # =====================================

    st.divider()

    st.header("📈 Financial Summary")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Total Expense",
            f"Rp {total_expense:,.0f}"
        )

    with col2:

        st.metric(
            "Remaining Balance",
            f"Rp {remaining:,.0f}"
        )

    # =====================================
    # FINANCIAL HEALTH SCORE
    # =====================================

    if total_expense <= income * 0.5:

        score = 90

    elif total_expense <= income * 0.8:

        score = 70

    else:

        score = 50

    st.metric(
        "Financial Health Score",
        f"{score}/100"
    )

    st.divider()

    # =====================================
    # SMART FINANCIAL INSIGHTS
    # =====================================

    st.header("🧠 Smart Financial Insights")

    insights = generate_smart_insights(
        income,
        total_expense,
        remaining,
        profile
    )

    for insight in insights:

        st.write(insight)

    st.divider()

    # =====================================
    # EXPENSE DATAFRAME
    # =====================================

    expense_data = pd.DataFrame({

        "Category": [
            "Food",
            "Transport",
            "Entertainment"
        ],

        "Amount": [
            food,
            transport,
            entertainment
        ]
    })

    # =====================================
    # BAR CHART
    # =====================================

    st.header("📊 Expense Visualization")

    st.bar_chart(
        expense_data.set_index("Category")
    )

    # =====================================
    # WARNING / SUCCESS MESSAGE
    # =====================================

    if total_expense > budget["Kebutuhan Pokok"]:

        st.warning(
            "⚠️ Your spending exceeds recommended basic needs allocation."
        )

    else:

        st.success(
            "✅ Your spending is still within safe allocation."
        )

    st.divider()

    # =====================================
    # AI FINANCIAL ADVISOR
    # =====================================

    st.header("🤖 AI Financial Advisor")

    if st.button(
        "Generate AI Financial Advice",
        key="ai_button"
    ):

        advice = generate_budget_advice(
            income,
            total_expense,
            remaining
        )

        st.write(advice)

    st.divider()

    # =====================================
    # FINANCIAL REPORT GENERATOR
    # =====================================

    st.header("📄 Financial Report")

    report = generate_financial_report(
        income,
        total_expense,
        remaining,
        score,
        profile
    )

    st.text_area(
        "Financial Report Preview",
        report,
        height=350
    )

    st.download_button(
        label="📥 Download Financial Report",
        data=report,
        file_name="financial_report.txt",
        mime="text/plain"
    )

    st.divider()

    # =====================================
    # CSV UPLOAD SECTION
    # =====================================

    st.header("📂 Upload Transaction CSV")

    uploaded_file = st.file_uploader(
        "Upload your transaction file",
        type=["csv"]
    )

    # =====================================
    # CSV ANALYSIS
    # =====================================

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.subheader("Transaction Data")

        st.dataframe(df)

        # =================================
        # ANALYSIS
        # =================================

        analysis = analyze_expenses(df)

        st.divider()

        st.subheader("📊 Expense Analysis")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Total CSV Expense",
                f"Rp {analysis['total_expense']:,.0f}"
            )

            st.metric(
                "Highest Expense Category",
                analysis["highest_category"]
            )

        with col2:

            st.metric(
                "Highest Expense Amount",
                f"Rp {analysis['highest_amount']:,.0f}"
            )

            st.metric(
                "Average Expense",
                f"Rp {analysis['average_expense']:,.0f}"
            )

        # =================================
        # CSV BAR CHART
        # =================================

        st.divider()

        st.subheader("📈 CSV Expense Visualization")

        csv_chart = df.groupby(
            "Category"
        )["Amount"].sum()

        st.bar_chart(csv_chart)

        # =================================
        # AI CSV INSIGHT
        # =================================

        if st.button(
            "Generate AI CSV Analysis",
            key="csv_ai_button"
        ):

            ai_csv_advice = generate_budget_advice(
                income,
                analysis["total_expense"],
                remaining
            )

            st.subheader("🤖 AI CSV Financial Insight")

            st.write(ai_csv_advice)

    st.divider()

    # =====================================
    # AI FINANCIAL CHATBOT
    # =====================================

    st.header("💬 AI Financial Chatbot")

    # SESSION STATE

    if "chat_history" not in st.session_state:

        st.session_state.chat_history = []

    # CHAT INPUT

    user_question = st.chat_input(
        "Ask your financial question..."
    )

    # PROCESS CHAT

    if user_question:

        # SAVE USER MESSAGE

        st.session_state.chat_history.append(
            ("You", user_question)
        )

        # GENERATE AI RESPONSE

        bot_response = financial_chatbot(
            user_question,
            profile
        )

        # SAVE AI RESPONSE

        st.session_state.chat_history.append(
            ("AI", bot_response)
        )

    # DISPLAY CHAT HISTORY

    for sender, message in st.session_state.chat_history:

        if sender == "You":

            with st.chat_message("user"):

                st.write(message)

        else:

            with st.chat_message("assistant"):

                st.write(message)