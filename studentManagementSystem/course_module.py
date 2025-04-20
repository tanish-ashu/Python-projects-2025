from database.database_connection import create_connection, execute_query, fetch_data, close_connection

def add_course(course_id, course_name, credits, department):
    connection = create_connection()
    if connection:
        query = """
            INSERT INTO courses(course_id, course_name, credits, department) VALUES (%s, %s, %s, %s)
        """
        params = (course_id, course_name, credits, department)
        execute_query(connection, query, params)
        close_connection(connection)
        
        
def  view_courses():
    connection = create_connection()
    if connection:
        query = "SELECT * FROM courses"
        courses = fetch_data(connection, query)
        close_connection(connection)
    if courses:
        for course in courses:
            print(course)
    else:
        print("No courses found.")
        
        
def update_course(course_id, course_name, credits, department):
    connection = create_connection()
    if connection:
        query = """
            UPDATE courses 
            SET course_name = %s, credits = %s, department = %s 
            WHERE course_id = %s
        """
        params = (course_name, credits, department, course_id)
        execute_query(connection, query, params)
        close_connection(connection)
        
def delete_course(course_id):
    connection = create_connection()
    if connection:
        query = "DELETE FROM courses WHERE course_id = %s"
        params = (course_id,)
        execute_query(connection, query, params)
        close_connection(connection)
        

        
        


