import mysql.connector

def create_connection():
    try:
        connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "password",
            database = "studentmanagementsystem"
            )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    
    
    
    
    
def execute_query(connection, query, params = None):
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        return cursor.lastrowid # Return the Id of the last inserted row
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()
        
        
        

        
        
def fetch_data(connection, query, params = None):
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        cursor.close()
        
        
        
def close_connection(connection):
    if connection:
        connection.close()
        
        
        


