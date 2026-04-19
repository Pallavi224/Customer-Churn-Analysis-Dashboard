import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customer Churn Dashboard", layout="wide")

st.title("📉 Customer Churn Analysis Dashboard")

file = st.file_uploader("Upload Churn Dataset", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader("Raw Data")
    st.write(df.head())

    # ----------------------------
    # Data Cleaning
    # ----------------------------
    df.dropna(inplace=True)

    # Convert churn column to numeric if needed
    if df['Churn'].dtype == 'object':
        df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    # ----------------------------
    # KPIs
    # ----------------------------
    total_customers = df.shape[0]
    churned = df['Churn'].sum()
    churn_rate = (churned / total_customers) * 100
    avg_tenure = df['Tenure'].mean()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("👥 Total Customers", total_customers)
    col2.metric("❌ Churned Customers", int(churned))
    col3.metric("📉 Churn Rate (%)", f"{churn_rate:.2f}")
    col4.metric("⏱️ Avg Tenure (months)", f"{avg_tenure:.1f}")

    # ----------------------------
    # Filters
    # ----------------------------
    st.sidebar.header("Filters")

    if 'Subscription Type' in df.columns:
        subscription = st.sidebar.multiselect(
            "Subscription Type",
            options=df['Subscription Type'].unique(),
            default=df['Subscription Type'].unique()
        )
        df = df[df['Subscription Type'].isin(subscription)]

    if 'Contract Length' in df.columns:
        contract = st.sidebar.multiselect(
            "Contract Length",
            options=df['Contract Length'].unique(),
            default=df['Contract Length'].unique()
        )
        df = df[df['Contract Length'].isin(contract)]

    # ----------------------------
    # Charts
    # ----------------------------
    st.subheader("Churn Distribution")
    st.bar_chart(df['Churn'].value_counts())

    if 'Gender' in df.columns:
        st.subheader("Churn by Gender")
        gender_churn = df.groupby('Gender')['Churn'].mean() * 100
        st.bar_chart(gender_churn)

    if 'Total Spend' in df.columns:
        st.subheader("Total Spend vs Churn")
        spend_churn = df.groupby(pd.cut(df['Total Spend'], bins=10))['Churn'].mean() * 100
        spend_churn.index = spend_churn.index.astype(str)
        st.line_chart(spend_churn)

    if 'Subscription Type' in df.columns:
        st.subheader("Churn by Subscription Type")
        subscription_churn = df.groupby('Subscription Type')['Churn'].mean() * 100
        st.bar_chart(subscription_churn)

    if 'Support Calls' in df.columns:
        st.subheader("Support Calls vs Churn")
        support_churn = df.groupby('Support Calls')['Churn'].mean() * 100
        st.line_chart(support_churn)

    if 'Payment Delay' in df.columns:
        st.subheader("Payment Delay Distribution by Churn")
        fig = px.box(df, x='Churn', y='Payment Delay', title='Payment Delay by Churn Status')
        st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Upload a churn dataset to begin analysis")