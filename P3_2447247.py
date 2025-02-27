import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns

col1 , col2 = st.columns([1,3])

with col1:
    st.image("C:\\Users\\shobh\\Desktop\\shop.jpg")

with col2:
    st.title('P3: Streamlit for Retail Company Data Analysis')
    st.write("Find the best deals on electronics, clothing, and accessories. Browse our catalog and enjoy exclusive discounts!")

user_name = st.text_input("Enter your name to get a special discount:", "")

if st.button("Claim Offer 🎁"):
    if user_name:
        st.success(f"Congratulations, {user_name}! You have unlocked a 10% discount!")
    else:
        st.warning("Please enter your name to claim the offer.")

df= pd.read_csv("E:\\archive (14)\\shopping_behavior_updated.csv")
st.markdown("---")
st.subheader(":green[Before you buy], ***check out our data analysis dashboard*** below to make sure :rainbow[You are at the right place!]")

st.sidebar.title("Retail Company Data Analysis")
st.sidebar.write("This is a data analysis dashboard for a retail company.")

selected_category = st.sidebar.selectbox("Select a category",["All"]+ list(df['Category'].unique()))
selected_gender = st.sidebar.radio("Select Gender", ["All"] + df["Gender"].unique().tolist())

# Apply filters
filtered_df = df.copy()
if selected_category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == selected_category]
if selected_gender != "All":
    filtered_df = filtered_df[filtered_df["Gender"] == selected_gender]

# Dashboard Metrics
total_sales = filtered_df["Purchase Amount (USD)"].sum()
avg_purchase = filtered_df["Purchase Amount (USD)"].mean()
customer_count = filtered_df["Customer ID"].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales (USD)", f"${total_sales:,.2f}")
col2.metric("Average Purchase (USD)", f"${avg_purchase:,.2f}")
col3.metric("Unique Customers", customer_count)

# Progress Bar Example
progress_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.01)
    progress_bar.progress(percent_complete + 1)

# Bar Chart: Purchases by Category (Filtered)
st.subheader("Purchases by Category")
fig, ax = plt.subplots()
sns.barplot(data=filtered_df, x="Category", y="Purchase Amount (USD)", ax=ax, color="green")
plt.xticks(rotation=45)
st.pyplot(fig)

# Line Chart: Sales Trend Over Time (Filtered)
st.subheader("Sales Trend Over Time")
filtered_df["Purchase Date"] = pd.date_range(start="2023-01-01", periods=len(filtered_df), freq="D")

fig, ax = plt.subplots()
sns.lineplot(data=filtered_df, x="Purchase Date", y="Purchase Amount (USD)", hue="Category", ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

# Scatter Plot: Age vs. Purchase Amount (Filtered)
st.subheader("Customer Age vs. Purchase Amount")
fig, ax = plt.subplots()
sns.scatterplot(data=filtered_df, x="Age", y="Purchase Amount (USD)", hue="Category", size="Purchase Amount (USD)", ax=ax)
st.pyplot(fig)

# Slider Example: Age Selection
st.sidebar.subheader("Age Filter")
age_range = st.sidebar.slider("Select Age Range", int(df["Age"].min()), int(df["Age"].max()), (int(df["Age"].min()), int(df["Age"].max())))
filtered_df = filtered_df[(filtered_df["Age"] >= age_range[0]) & (filtered_df["Age"] <= age_range[1])]

# Checkbox Example: Show Raw Data
if st.sidebar.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(filtered_df)

# Radio Buttons: Payment Method
st.sidebar.subheader("Choose Payment Method")
payment_method = st.sidebar.radio("Payment Method", ["All"] + df["Payment Method"].unique().tolist())
if payment_method != "All":
    filtered_df = filtered_df[filtered_df["Payment Method"] == payment_method]

# Select Box: Shipping Type
st.sidebar.subheader("Select Shipping Type")
shipping_type = st.sidebar.selectbox("Shipping Type", ["All"] + df["Shipping Type"].unique().tolist())
if shipping_type != "All":
    filtered_df = filtered_df[filtered_df["Shipping Type"] == shipping_type]

# Text Input Example: Feedback
user_feedback = st.text_input("Provide your feedback about this dashboard")
if st.button("Submit Feedback"):
    st.success("Thank you for your feedback!")

st.sidebar.write("### Thank you for exploring the dashboard!")