import mysql.connector
from mysql.connector import Error

def init_db():
    """Initialize the MySQL database and create travel_options table."""
    try:
        # Connect to MySQL server (without specifying a database)
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root'
        )
        cursor = conn.cursor()

        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS green_journey")
        print("Database 'green_journey' created or already exists.")

        # Switch to the database
        cursor.execute("USE green_journey")

        # Create travel_options table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS travel_options (
                id INT AUTO_INCREMENT PRIMARY KEY,
                destination VARCHAR(255) NOT NULL,
                transport_mode VARCHAR(50) NOT NULL,
                carbon_footprint FLOAT NOT NULL
            )
        """)
        print("Table 'travel_options' created or already exists.")

        # Insert sample data
        cursor.execute("SELECT COUNT(*) FROM travel_options")
        count = cursor.fetchone()[0]
        if count == 0:
            sample_data = [
                ('Paris', 'Train', 0.05),
                ('London', 'Bicycle', 0.01),
                ('Amsterdam', 'Electric Car', 0.1)
            ]
            cursor.executemany(
                "INSERT INTO travel_options (destination, transport_mode, carbon_footprint) VALUES (%s, %s, %s)",
                sample_data
            )
            conn.commit()
            print("Inserted sample data into travel_options.")

        cursor.close()
        conn.close()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn.is_connected():
            conn.close()
            print("MySQL connection closed.")

if __name__ == '__main__':
    init_db()