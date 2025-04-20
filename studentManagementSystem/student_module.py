from database.database_connection import create_connection, execute_query, fetch_data, close_connection


def add_student(first_name, last_name, date_of_birth, address, phone_number, email, enrollment_date):
    connection = create_connection()
    if connection:
        query = """
            INSERT INTO students(first_name, last_name, date_of_birth, address, phone_number, email, enrollment_date)
            VALUES (%s ,%s, %s, %s, %s, %s, %s)
            """
        params = (first_name, last_name, date_of_birth, address, phone_number, email, enrollment_date)
        execute_query(connection,query,params)
        close_connection(connection)
            
            
            
            
            
def view_students():
    connection = create_connection()
    if connection: 
        query = "SELECT * FROM students"
        students = fetch_data(connection,query)
        close_connection(connection)
    if students:
        for student in students:
            print(student)
    else:
        print("No students found.")
        
        
        
        
def update_student(student_id, first_name, last_name, date_of_birth, address, phone_number, email, enrollment_date):
    connection = create_connection()
    if connection:
        query = """
           UPDATE students
           SET fitst_name = %s, last_name = %s, date_of_birth = %s, address = %s, phone_number = %s, email = %s, enrollment_date =%s
           WHERE student_id = %s
          """
        params = (first_name, last_name, date_of_birth, address, phone_number, email, enrollment_date, student_id)
        execute_query(connection,query,params)
        close_connection(connection)
        
        
        
def delete_student(student_id):
    connection = create_connection()
    if connection:
        query = "DELETE FROM students WHERE student_id = %s"
       # %s is a placeholder (not Python's f-string!).
       #Works with mysql-connector, psycopg2, etc.
       # Prevents SQL injection (safer than hardcoding values).
        params = (student_id,)   
        # Without the comma, (student_id_to_delete) is just a parenthesized integer, not a tuple.
        # SQL parameterized queries require a tuple/list for params, even with one value.
        execute_query(connection, query, params)
        close_connection(connection)

        
        
        
         
