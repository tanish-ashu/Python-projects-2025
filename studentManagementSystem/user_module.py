from database.database_connection import create_connection, execute_query, fetch_data, close_connection

def create_user(username, password, role):
    connection = create_connection()
    if connection:
        query = "INSERT INTO users (username, password, role), VALUES ( %s, %s, $s)"
        params = (username, password, role) 
        execute_query(connection, query, params)
        close_connection(connection)
        
        
def authenticate_user(username, password):
    connection = create_connection()
    if connection:
        query = "SELECT * FROM users WHERE user_name = %s"
        params = (username,)
        user = fetch_data(connection,query, params)
        close_connection(connection)
        if user:
            stored_password = user[0][2]
            if password == stored_password:
                return user[0] # Return user data
        return None
    
