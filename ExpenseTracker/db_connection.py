import mysql.connector
from mysql.connector import Error

def create_db_connection():
    """ Creates and returns a connection to the MySQL database. """
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",       
            user="root",   
            password="password",
            database="expenseTracker" 
        )
        print("MySQL Database connection successful")
    except Error as e:
        print(f"Error: '{e}'")
        print("Could not connect to the database. Please check credentials and ensure MySQL server is running.")
        exit() # Stops the script if connection fails as no code will work without it

    return connection


