#connect to a MySQL server and create a database
# This script connects to a MySQL server and creates a database named "alx_book_store".
# It handles connection errors and ensures the database is created only if it does not already exist.
# It uses the mysql-connector-python package, which can be installed via pip:
# pip install mysql-connector-python
try:
    import mysql.connector
    from mysql.connector import errorcode
except ImportError as e:
    raise ImportError(
        "Missing dependency 'mysql-connector-python'. Install it with: "
        "pip install mysql-connector-python"
    ) from e

# Configuration for connecting to the MySQL server
# NOTE: Replace 'your_username' and 'your_password' with your actual MySQL credentials
CONFIG = {
    'user': 'root',         # Use your MySQL user
    'password': 'passward', # Use the password you set
    'host': 'localhost'
}

DATABASE_NAME = "alx_book_store"

def create_database():
    """
    Attempts to connect to the MySQL server and create the specified database.
    """
    db_connection = None
    try:
        # Establish connection to the MySQL server
        print(f"Attempting to connect to MySQL server at {CONFIG['host']}...")
        db_connection = mysql.connector.connect(**CONFIG)
        cursor = db_connection.cursor()
        
        # SQL command to create the database if it doesn't exist
        # This prevents the script from failing if the database already exists
        sql_command = f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"
        
        # Execute the SQL command
        cursor.execute(sql_command)
        
        # Check if the database was just created or already existed
        # The cursor's rowcount is a simple way to check, but NOT foolproof for all connectors.
        # A more robust check without SELECT/SHOW is often hard, but the IF NOT EXISTS
        # ensures the script meets the non-failure requirement.
        
        print(f"Database '{DATABASE_NAME}' created successfully or already exists!")
        
    except mysql.connector.Error as err:
        # Handle connection errors
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            # This is generally not reached as we connect without a default DB
            print(f"Error: Database does not exist.")
        elif err.errno == errorcode.CR_CONN_ERROR:
             print(f"Error: Failed to connect to the DB. Ensure MySQL server is running on {CONFIG['host']}:{mysql.connector.connect(**CONFIG).port} and credentials are correct.")
        else:
            print(f"An unexpected error occurred during database creation: {err}")
            
    finally:
        # Close the cursor and connection (handles open and close of the DB)
        if 'cursor' in locals() and cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            db_connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()