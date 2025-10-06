from sqlalchemy import create_engine
import pandas as pd

# Replace with your database details
username = "root"
password = "root"
host = "localhost"
port = "3306"
database = "classicmodels"

# SQLAlchemy connection string
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

# Example query
query = "SELECT * FROM employees;"
query1 = "SELECT * FROM customers;"
query2 = "SELECT * FROM orders;"
query3 = "SELECT * FROM orderdetails;"
query4 = "SELECT * FROM products;"

# Read query directly into a pandas DataFrame
df = pd.read_sql(query, engine)
df1 = pd.read_sql(query1, engine)
df2 = pd.read_sql(query2, engine)
df3 = pd.read_sql(query3, engine)
df4 = pd.read_sql(query4, engine)

m1 = pd.merge(df1, df2, on='customerNumber', how='inner')
m2 = pd.merge(m1, df3, on='orderNumber', how='inner')
m3 = pd.merge(m2, df4, on='productCode', how='inner')
print(m3.head().to_string())
print(m3.shape)
