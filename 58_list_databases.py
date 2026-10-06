# 58. Get a list of existing databases
# Install connector first: pip install mysql-connector-python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = conn.cursor()
cursor.execute("SHOW DATABASES")

print("Existing Databases:")
for db in cursor:
    print(db[0])

cursor.close()
conn.close()
