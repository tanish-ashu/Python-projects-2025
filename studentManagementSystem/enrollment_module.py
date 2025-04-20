from database.database_connection import create_connection , execute_query, fetch_data, close_connection


def enroll_student(student_id, course_id, grade):
    connection = create_connection()
    if connection:
        query = """
            INSERT INTO enrollments(student_id, course_id, grade) VALUES( %s, %s, %s)
        """
        params = (student_id, course_id, grade)
        execute_query(connection, query, params)
        close_connection(connection)


def view_enrollments():
    connection = create_connection()
    if connection:
        query = """
             SELECT e.enrollment_id, s.first_name, s.last_name, c.course_name, e.grade
             FROM enrollments e
             JOIN students s ON e.student_id = s.student_id
             JOIN courses c ON e.course_id = c.course_id
        """
        
        enrollments = fetch_data(connection, query)
        close_connection(connection)
        if enrollments:
            for enrollment in enrollments:
                print(enrollment)
        else:
            print("No enrollments found")
            
            
            
def update_enrollment(enrollment_id, student_id, course_id, grade):
    connection = create_connection()
    if connection:
        query = """
            UPDATE emrollments
            SET student_id = %s, course_id = %s, grade = %s 
            WHERE enrollment_id = %s
        """
        params = (student_id, course_id, grade, enrollment_id)
        execute_query(connection, query, params)
        close_connection(connection)
        
        
def delete_enrollment(enrollment_id):
    connection = create_connection()
    if connection:
        query = """
            DELETE FROM enrollments WHERE enrollment_id = %s
        """
        params = (enrollment_id,)
        execute_query(connection, query, params)
        close_connection(connection)
        
        