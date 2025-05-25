import streamlit as st
from services import file_handler, analyzer, gpt_budgeter, predictor
from components import charts

st.set_page_config(page_title="AI Personal Finance Advisor")

st.title("📊 AI-Based Personal Finance Advisor")
file = st.file_uploader("Upload your bank statement", type=['csv', 'xlsx'])

if file:
    df = file_handler.parse_statement(file)
    summary, top_categories = analyzer.summarize_spending(df)

    st.subheader("Spending Over Time")
    charts.show_spending_chart(summary)

    st.subheader("Top Spending Categories")
    st.write(top_categories)

    st.subheader("GPT-4 Budgeting Tips")
    st.markdown(gpt_budgeter.generate_budget_tips(summary, top_categories))

    st.subheader("Cash Flow Forecast")
    future = predictor.predict_future_cash_flow(df)
    st.line_chart(future)
