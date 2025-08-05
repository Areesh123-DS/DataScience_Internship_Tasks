import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# App config
st.set_page_config(page_title="Global Superstore Dashboard", layout="wide")
st.title("📊 Global Superstore Performance Dashboard")

# Custom CSS: background, font, heading italic, purple pills
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f4f0fa;
        font-family: 'Segoe UI', sans-serif;
    }
    h2 {
        font-style: italic !important;
    }
    /* Purple pill color for selected items */
    .css-1n76uvr, .css-1p3m7a8, .css-q8sbsg {
        background-color: #a855f7 !important; /* purple */
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load dataset without cache
def load_data():
    df = pd.read_csv("Global_Superstore2.csv", encoding='ISO-8859-1')
    df = df.dropna(subset=['Sales', 'Profit'])
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month_name()
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("📌 *Filters*")
region = st.sidebar.multiselect("Select Region", options=df['Region'].unique(), default=df['Region'].unique())
category = st.sidebar.multiselect("Select Category", options=df['Category'].unique(), default=df['Category'].unique())

# Apply filters
filtered_df = df[(df['Region'].isin(region)) & (df['Category'].isin(category))]
top_customers = filtered_df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(5)

# KPIs
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
col2.metric("📈 Total Profit", f"${total_profit:,.2f}")
col3.metric("👤 Top Customer", top_customers.idxmax())

st.markdown("---")

# 📦 Sales by Category (purple)
st.subheader("_📦 Sales by Category_")
fig1, ax1 = plt.subplots()
category_sales = filtered_df.groupby('Category')['Sales'].sum().reset_index()
sns.barplot(data=category_sales, x='Category', y='Sales', color="purple", ax=ax1)
ax1.set_title("Total Sales per Category")
ax1.tick_params(axis='x', rotation=0)
st.pyplot(fig1)

# 🌍 Profit by Region (gold)
st.subheader("_🌍 Profit by Region_")
fig2, ax2 = plt.subplots()
region_profit = filtered_df.groupby('Region')['Profit'].sum().reset_index()
sns.barplot(data=region_profit, x='Region', y='Profit', color="gold", ax=ax2)
ax2.set_title("Total Profit per Region")
ax2.tick_params(axis='x', rotation=30)
st.pyplot(fig2)

# 🏅 Top 5 Customers (hot pink)
st.subheader("_🏅 Top 5 Customers by Sales_")
fig3, ax3 = plt.subplots()
sns.barplot(x=top_customers.values, y=top_customers.index, color='hotpink', ax=ax3)
ax3.set_title("Top 5 Customers")
ax3.set_xlabel("Sales")
st.pyplot(fig3)

# ⏳ Sales over time (rotate dates clearly)
st.subheader("_⏳ Monthly Sales Trend_")

# Group data monthly
monthly_sales = filtered_df.groupby(pd.Grouper(key='Order Date', freq='ME'))['Sales'].sum().reset_index()
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=monthly_sales, x='Order Date', y='Sales', color='teal', ax=ax)
ax.set_title("Monthly Sales Over Time")
ax.set_xlabel("Order Date")
ax.set_ylabel("Sales")

# Rotate x-axis labels to prevent overlapping
plt.xticks(rotation=45)

st.pyplot(fig)


# 📍 Scatterplot
st.subheader("_📍 Profit vs Sales Scatterplot_")
fig5, ax5 = plt.subplots()
sns.scatterplot(data=filtered_df, x='Sales', y='Profit', hue='Category', palette="Set2", ax=ax5)
ax5.set_title("Profit vs Sales by Category")
st.pyplot(fig5)

# Summary
st.markdown("### 📝 Summary Insights")
st.write("- 🎯 The dashboard is interactive. Try changing the filters to explore insights.")
st.write("- 📌 High-profit segments or underperforming sub-categories can be determined")

st.markdown(
    """
    <div style="text-align:center; padding-top: 20px;">
        <span style="color:gray;">© 2025 Business Intelligence Dashboard</span>
    </div>
    """,
    unsafe_allow_html=True
)
