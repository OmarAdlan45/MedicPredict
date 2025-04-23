import mysql.connector

# Attempt to establish a connection (update with your own credentials)
try:
    connection = mysql.connector.connect(
        host="your_host",
        user="your_username",
        password="your_password",
        database="your_database"
    )
    if connection.is_connected():
        print("Successfully connected to MySQL database")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if connection.is_connected():
        connection.close()
