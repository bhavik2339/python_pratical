# 62. Update student information
import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="root", password="", database="dbStudent"
)
cursor = conn.cursor()

sql = """UPDATE tblStudInfo
SET student_name=%s, stream=%s, contact_number=%s, remarks=%s
WHERE student_id=%s"""

values = ("Milan R Ghodasara", "BCA", "9999999999", "Updated", 1)

cursor.execute(sql, values)
conn.commit()

print(cursor.rowcount, "student record updated.")
cursor.close()
conn.close()
