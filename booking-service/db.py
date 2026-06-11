import mysql.connector
import time

connection = None

for i in range(10):
    try:
        connection = mysql.connector.connect(
            host="mysql",
            user="root",
            password="root",
            database="airline_db"
        )
        print("Connected to MySQL")
        break

    except Exception as e:
        print("Waiting for MySQL...")
        time.sleep(5)

cursor = connection.cursor()