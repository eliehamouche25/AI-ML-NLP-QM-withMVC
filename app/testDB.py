
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="elie",
    database="myprojectdb"
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()