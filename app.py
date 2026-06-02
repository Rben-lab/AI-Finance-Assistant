# Import required libraries
import streamlit as st
import pandas as pd

# Import custom modules
from modules.budget import calculate_budget
from modules.ai_advisor import generate_budget_advice
from modules.analysis import analyze_expenses
from modules.chatbot import financial_chatbot
from modules.insight import generate_smart_insights
from modules.report import generate_financial_report

# Configure Streamlit page settings
st.set_page_config(
    page_title="AI Finance Assistant",
    layout="wide"
)

# Main application title
st.title("💰 AI-Powered Personal Finance Assistant")

# User monthly income input
st.header("Monthly Income")

income = st.number_input(
    "Enter your monthly income",
    min_value=0,
    step=100000,
    key="income_input"
)

# Financial profile selection
profile = st.selectbox(
    "Choose Financial Profile",
    [
        "Student Investor",
        "Balanced",
        "Conservative"
    ],
    key="profile_select"
)

# Run application after income is entered
if income > 0:

    # Generate recommended budget allocation
    budget = calculate_budget(
        income,
        profile
    )

    st.header("📊 Recommended Budget Allocation")

    columns = st.columns(len(budget))

    # Display budget allocation metrics
    for col, (category, amount) in zip(columns, budget.items()):

        with col:

            st.metric(
                category,
                f"Rp {amount:,.0f}"
            )

    st.divider()

    # User expense inputs
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

    # Calculate expenses and remaining balance
    total_expense = (
        food +
        transport +
        entertainment
    )

    remaining = income - total_expense

    st.divider()

    # Financial summary section
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

    # Generate simple financial health score
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

    # Generate smart financial insights
    st.header("🧠 Smart Financial Insights")

    insights = generate_smart_insights(
        income,
        total_expense,
        remaining,
        profile
    )

    # Display AI-generated insights
    for insight in insights:

        st.write(insight)

    st.divider()

    # Create expense dataframe
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

    # Visualize expenses using bar chart
    st.header("📊 Expense Visualization")

    st.bar_chart(
        expense_data.set_index("Category")
    )

    # Display spending warning or success message
    if total_expense > budget["Kebutuhan Pokok"]:

        st.warning(
            "⚠️ Your spending exceeds recommended basic needs allocation."
        )

    else:

        st.success(
            "✅ Your spending is still within safe allocation."
        )

    st.divider()

    # AI-generated financial recommendation
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

    # Generate downloadable financial report
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

    # Download report as text file
    st.download_button(
        label="📥 Download Financial Report",
        data=report,
        file_name="financial_report.txt",
        mime="text/plain"
    )

    st.divider()

    # CSV upload section
    st.header("📂 Upload Transaction CSV")

    uploaded_file = st.file_uploader(
        "Upload your transaction file",
        type=["csv"]
    )

    # Process uploaded CSV file
    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.subheader("Transaction Data")

        st.dataframe(df)

        # Analyze uploaded transaction data
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

        st.divider()

        # CSV expense visualization
        st.subheader("📈 CSV Expense Visualization")

        csv_chart = df.groupby(
            "Category"
        )["Amount"].sum()

        st.bar_chart(csv_chart)

        # Generate AI analysis from CSV data
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

    # AI financial chatbot section
    st.header("💬 AI Financial Chatbot")

    # Store chat history using session state
    if "chat_history" not in st.session_state:

        st.session_state.chat_history = []

    # Chat input field
    user_question = st.chat_input(
        "Ask your financial question..."
    )

    # Process user question
    if user_question:

        # Save user message
        st.session_state.chat_history.append(
            ("You", user_question)
        )

        # Generate chatbot response
        bot_response = financial_chatbot(
            user_question,
            profile
        )

        # Save AI response
        st.session_state.chat_history.append(
            ("AI", bot_response)
        )

    # Display conversation history
    for sender, message in st.session_state.chat_history:

        if sender == "You":

            with st.chat_message("user"):

                st.write(message)

        else:

            with st.chat_message("assistant"):

                st.write(message)
