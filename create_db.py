import sqlite3
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
import random

# Define the database connection
DATABASE_URL = "sqlite:///retail.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Define the tables
class Product(Base):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    price = Column(Float)

class Sale(Base):
    __tablename__ = "sales"
    sale_id = Column(Integer, primary_key=True)
    product_id = Column(Integer)
    quantity = Column(Integer)
    sale_date = Column(Date)
    store_id = Column(Integer)

class Inventory(Base):
    __tablename__ = "inventory"
    product_id = Column(Integer, primary_key=True)
    store_id = Column(Integer)
    stock_quantity = Column(Integer)

class Store(Base):
    __tablename__ = "stores"
    store_id = Column(Integer, primary_key=True)
    store_name = Column(String)
    location = Column(String)

# Create the tables
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Sample Data (Using Pandas DataFrames for easier insertion)
products_data = {
    "product_id": [1, 2, 3, 4, 5],
    "name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
    "category": ["Electronics", "Accessories", "Accessories", "Electronics", "Accessories"],
    "price": [1200.0, 25.0, 50.0, 300.0, 80.0],
}
products_df = pd.DataFrame(products_data)
products_df.to_sql("products", engine, if_exists="replace", index=False) # Changed to replace

stores_data = {
    "store_id": [1, 2, 3],
    "store_name": ["Store A", "Store B", "Store C"],
    "location": ["City X", "City Y", "City Z"],
}
stores_df = pd.DataFrame(stores_data)
stores_df.to_sql("stores", engine, if_exists="replace", index=False) # Changed to replace

inventory_data = {
    "product_id": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    "store_id": [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],
    "stock_quantity": [100, 200, 150, 80, 300, 50, 100, 75, 40, 150, 120, 250, 180, 90, 350],
}
inventory_df = pd.DataFrame(inventory_data)
inventory_df.to_sql("inventory", engine, if_exists="replace", index=False) # Changed to replace

# Create some sample sales data with dates.
sales_list = []
for i in range(100):
  sale_id = 1000 + i
  product_id = random.choice([1,2,3,4,5])
  quantity = random.randint(1,10)
  sale_date = datetime.now() - timedelta(days=random.randint(0, 30))
  store_id = random.choice([1,2,3])
  sales_list.append([sale_id, product_id, quantity, sale_date, store_id])

sales_df = pd.DataFrame(sales_list, columns = ['sale_id', 'product_id', 'quantity', 'sale_date', 'store_id'])
sales_df.to_sql('sales', engine, if_exists = 'append', index = False) # Sales can append since it is new data.

session.close()

print("Database and tables created/updated successfully!")