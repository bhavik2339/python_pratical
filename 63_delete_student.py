# 63. Delete student information
import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="root", password="", database="dbStudent"
)
cursor = conn.cursor()

student_id = 1
cursor.execute("DELETE FROM tblStudInfo WHERE student_id=%s", (student_id,))
conn.commit()

print(cursor.rowcount, "student record deleted.")
cursor.close()
conn.close()
