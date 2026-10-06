# 58. Insert a row into a table
# Assumes database "testdb" and table "student(id, name, age)"
import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="root", password="", database="testdb"
)
cursor = conn.cursor()

sql = "INSERT INTO student (id, name, age) VALUES (%s, %s, %s)"
values = (1, "Milan", 20)

cursor.execute(sql, values)
conn.commit()

print(cursor.rowcount, "row inserted.")
cursor.close()
conn.close()
