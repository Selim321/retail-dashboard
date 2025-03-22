import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px
from datetime import datetime, timedelta

# Database connection
DATABASE_URL = "sqlite:///retail.db"
engine = create_engine(DATABASE_URL)

# Function to fetch data from the database
def fetch_data(query):
    return pd.read_sql(query, engine)

# Streamlit app
st.title("Retail Sales & Inventory Dashboard with Forecasting")

# Sales Data Analysis
st.header("Sales Analysis")

# Date Range Filter
today = datetime.now().date()
start_date = st.date_input("Start Date", today - timedelta(days=30)) #increased range for forecasting
end_date = st.date_input("End Date", today)

# Sales Data
sales_query = f"""
SELECT s.sale_date, s.quantity, p.name AS product_name, p.category, st.store_name
FROM sales s
JOIN products p ON s.product_id = p.product_id
JOIN stores st ON s.store_id = st.store_id
WHERE s.sale_date BETWEEN '{start_date}' AND '{end_date}'
"""
sales_df = fetch_data(sales_query)

if not sales_df.empty:
    # Sales by Product Chart
    sales_by_product = sales_df.groupby("product_name")["quantity"].sum().reset_index()
    fig_sales_product = px.bar(sales_by_product, x="product_name", y="quantity", title="Sales by Product")
    st.plotly_chart(fig_sales_product)

    # Sales by Store Chart
    sales_by_store = sales_df.groupby("store_name")["quantity"].sum().reset_index()
    fig_sales_store = px.bar(sales_by_store, x="store_name", y="quantity", title="Sales by Store")
    st.plotly_chart(fig_sales_store)

    # Sales over time
    sales_by_date = sales_df.groupby('sale_date')['quantity'].sum().reset_index()
    fig_sales_time = px.line(sales_by_date, x='sale_date', y='quantity', title="Sales over Time")
    st.plotly_chart(fig_sales_time)

    # Sales by Category chart
    sales_by_category = sales_df.groupby('category')['quantity'].sum().reset_index()
    fig_sales_category = px.pie(sales_by_category, values='quantity', names='category', title='Sales by Category')
    st.plotly_chart(fig_sales_category)

    # Sales Forecasting (Simple Moving Average)
    st.header("Sales Forecasting (7-Day Moving Average)")

    sales_by_date_forecast = sales_df.groupby('sale_date')['quantity'].sum().reset_index()
    sales_by_date_forecast['moving_average'] = sales_by_date_forecast['quantity'].rolling(window=7).mean()

    fig_forecast = px.line(sales_by_date_forecast, x='sale_date', y=['quantity', 'moving_average'], title='Sales Forecasting (7-Day Moving Average)')
    st.plotly_chart(fig_forecast)

else:
    st.write("No sales data available for the selected date range.")

# Inventory Data
st.header("Inventory Levels")

inventory_query = """
SELECT i.stock_quantity, p.name AS product_name, st.store_name
FROM inventory i
JOIN products p ON i.product_id = p.product_id
JOIN stores st ON i.store_id = st.store_id
"""
inventory_df = fetch_data(inventory_query)

if not inventory_df.empty:
    # Inventory Levels Table
    st.dataframe(inventory_df)
else:
    st.write("No inventory data available.")