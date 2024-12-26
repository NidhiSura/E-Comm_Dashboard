from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# Function to fetch data
def fetch_data(query):
    conn = sqlite3.connect('data/ecommerce.db')
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/api/sales', methods=['GET'])
def sales_data():
    query = """
    SELECT 
        InvoiceDate, 
        UnitPrice * Quantity AS NetPrice,
        Country 
    FROM orders 
    GROUP BY InvoiceDate
    """
    data = fetch_data(query)
    result = [{"date": row[0], "sales": row[1], "category": row[2]} for row in data]
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
