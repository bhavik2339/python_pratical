# 61. Create dbStudent and tblStudInfo, then insert student information
import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="root", password=""
)
cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS dbStudent")
cursor.execute("USE dbStudent")

cursor.execute("""
CREATE TABLE IF NOT EXISTS tblStudInfo (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    stream VARCHAR(50),
    college_name VARCHAR(150),
    contact_number VARCHAR(20),
    remarks VARCHAR(255)
)
""")

sql = """INSERT INTO tblStudInfo
(student_id, student_name, stream, college_name, contact_number, remarks)
VALUES (%s, %s, %s, %s, %s, %s)"""

values = (1, "Milan", "BCA", "Kamani Science College", "9999999999", "Good")
cursor.execute(sql, values)
conn.commit()

print("Database/table created and student information inserted.")
cursor.close()
conn.close()
