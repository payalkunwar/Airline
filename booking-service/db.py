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

cursor.execute("""
CREATE TABLE IF NOT EXISTS bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    passenger_name VARCHAR(255),
    flight_number VARCHAR(50)
)
""")

connection.commit()