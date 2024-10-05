import mysql.connector as conn

def connect_and_create_db():
    connection = None
    try:
        # Defining connection parameters
        connection = conn.connect(
            host = "***",
            port = "3306",
            user = "***",
            password = "***"
        )
        if connection.is_connected():
            print("Successfully connected to RDS instance")
            cursor = connection.cursor()

            # Creating Database (temp_db)
            cursor.execute("CREATE DATABASE IF NOT EXISTS temp_db")
            print("Database created successfully")
            cursor.execute("SHOW DATABASES")
            print(cursor.fetchall())
        else:
            print("Failed to connect RDS instance")
    except conn.Error as e:
        print(f"Error: {e}")
    finally:
        # Closing connection after the task of creation
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection is closed")


if __name__ == "__main__":
    connect_and_create_db()