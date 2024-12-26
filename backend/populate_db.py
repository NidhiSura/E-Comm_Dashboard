import sqlite3
import pandas as pd

# Load dataset
df = pd.read_excel('data/Online_Retail.xlsx')

# Connect to SQLite database
conn = sqlite3.connect('data/ecommerce.db')
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    InvoiceNo INTEGER PRIMARY KEY,
    StockCode TEXT,
    Description TEXT,
    Quantity INTEGER,
    InvoiceDate TEXT,
    UnitPrice INTEGER,
    CustomerID INTEGER,
    Country TEXT
)
""")

# Insert data
df.to_sql('orders', conn, if_exists='replace', index=False)

print("Database populated successfully.")
conn.commit()
conn.close()