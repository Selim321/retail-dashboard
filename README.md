# Retail Sales & Inventory Dashboard

This project creates a Streamlit dashboard for visualizing retail sales and inventory data from an SQLite database. It provides insights into sales trends, inventory levels, and basic sales forecasting.

## Features

* **Sales Analysis:**
    * Interactive date range selection for sales data.
    * Visualizations of sales by product, store, category, and over time.
    * Simple sales forecasting using a 7-day moving average.
* **Inventory Levels:**
    * Table displaying current inventory levels for each product in each store.

## Technologies Used

* **Python:** The core programming language.
* **Streamlit:** For creating the interactive web dashboard.
* **SQLAlchemy:** For interacting with the SQLite database.
* **Pandas:** For data manipulation and analysis.
* **Plotly Express:** For creating interactive charts and visualizations.
* **SQLite:** For the database.

## Setup Instructions

1.  **Clone the Repository (if applicable):**
    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2.  **Install Dependencies:**
    ```bash
    pip install streamlit pandas sqlalchemy plotly
    ```

3.  **Create the Database:**
    * Run the `create_db.py` script to create the SQLite database and populate it with sample data:
        ```bash
        python create_db.py
        ```
    * This will create a `retail.db` file in your project directory.

4.  **Run the Streamlit Dashboard:**
    ```bash
    streamlit run dashboard.py
    ```
    * This will open the dashboard in your web browser.

## Access the Dashboard Online

The dashboard can also be accessed online at:

[https://selim321-retail-dashboard-dashboard-93rrru.streamlit.app/](https://selim321-retail-dashboard-dashboard-93rrru.streamlit.app/)

## Project Structure

* `create_db.py`: Python script to create the SQLite database and tables.
* `dashboard.py`: Python script containing the Streamlit dashboard application.
* `retail.db`: SQLite database file.
* `README.md`: This file.

## Improvements

* Add more interactive filters (e.g., product, store).
* Implement inventory level alerts (e.g., color-coding for low stock).
* Enhance sales forecasting with more advanced models.
* Add the ability to download reports.
* Error handling.