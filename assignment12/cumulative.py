import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("../db/lesson.db:)")

query = """SELECT o.order_id, SUM(oi.quantity * p.price) AS total_price
FROM orders 0
JOIN line_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
"""
df = pd.read_sql_query(query, conn)

def cumulative(row):
    totals_above = df['total_price'][0:row.name+1]
    return totals_above.sum()

df['cumulative'] = df.apply(cumulative, axis=1)

plt.plt(df["order_id"], df["cumulative"], marker = "o")
plt.title("Cumulative Revenue by Order ID")
plt.xlabel("Order ID")
plt.ylabel("Cumulative Revenue")
plt.show()