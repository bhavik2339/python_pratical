# 59. Update a row in a table
import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="root", password="", database="testdb"
)
cursor = conn.cursor()

sql = "UPDATE student SET age=%s WHERE id=%s"
values = (21, 1)

cursor.execute(sql, values)
conn.commit()

print(cursor.rowcount, "row updated.")
cursor.close()
conn.close()
