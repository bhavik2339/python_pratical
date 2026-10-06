# 60. Delete a row from a table
import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="root", password="", database="testdb"
)
cursor = conn.cursor()

sql = "DELETE FROM student WHERE id=%s"
cursor.execute(sql, (1,))
conn.commit()

print(cursor.rowcount, "row deleted.")
cursor.close()
conn.close()
