from student_module import add_student, view_students, update_student, delete_student
from course_module import add_course, view_courses, update_course, delete_course
from enrollment_module import enroll_student, view_enrollments, update_enrollment, delete_enrollment
from user_module import create_user, authenticate_user
import datetime

def main():
    logged_in_user = None

    while True:
        if not logged_in_user:
            print("\nLogin/Sign Up")
            print("1. Login")
            print("2. Sign Up")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                username = input("Username: ")
                password = input("Password: ")
                logged_in_user = authenticate_user(username, password)
                if not logged_in_user:
                    print("Login failed. Please try again.")
            elif choice == "2":
                username = input("Username: ")
                password = input("Password: ")
                role = input("Role (admin/student/teacher): ")
                create_user(username, password, role)
                print("User created successfully. Please log in.")
            elif choice == "3":
                break
            else:
                print("Invalid choice.")
        else:
            print(f"\nWelcome, {logged_in_user[1]}!")
            while True:
                print("\nStudent Management System")
                print("1. Add Student")
                print("2. View Students")
                print("3. Update Student")
                print("4. Delete Student")
                print("5. Add Course")
                print("6. View Courses")
                print("7. Update Course")
                print("8. Delete Course")
                print("9. Enroll Student")
                print("10. View Enrollments")
                print("11. Update Enrollment")
                print("12. Delete Enrollment")
                print("13. Create User (Admin Only)")
                print("14. Logout")
                print("15. Exit")

                choice = input("Enter your choice: ")
                if choice == "13" and logged_in_user[3] != "admin":
                    print("You do not have permission to create users.")
                    continue
                if choice == "4" and logged_in_user[3] != "admin":
                    print("You do not have permission to delete students.")
                    continue
                if choice == "8" and logged_in_user[3] != "admin":
                    print("You do not have permission to delete courses.")
                    continue
                if choice == "12" and logged_in_user[3] != "admin":
                    print("You do not have permission to delete enrollments.")
                    continue
                if choice == "14":
                    logged_in_user = None
                    print("Logged out.")
                    break
                if choice == "15":
                    return

                if choice == "1":
                    first_name = input("First Name: ")
                    last_name = input("Last Name: ")
                    date_of_birth = input("Date of Birth (YYYY-MM-DD): ")
                    address = input("Address: ")
                    phone_number = input("Phone Number: ")
                    email = input("Email: ")
                    enrollment_date = datetime.date.today()
                    add_student(first_name, last_name, date_of_birth, address, phone_number, email, enrollment_date)
                    print("Student added successfully.")
                elif choice == "2":
                    view_students()
                elif choice == "3":
                    student_id = int(input("Student ID to update: "))
                    first_name = input("First Name: ")
                    last_name = input("Last Name: ")
                    date_of_birth = input("Date of Birth (YYYY-MM-DD): ")
                    address = input("Address: ")
                    phone_number = input("Phone Number: ")
                    email = input("Email: ")
                    enrollment_date = datetime.date.today()
                    update_student(student_id, first_name, last_name, date_of_birth, address, phone_number, email, enrollment_date)
                    print("Student updated successfully.")
                elif choice == "4":
                    student_id = int(input("Student ID to delete: "))
                    delete_student(student_id)
                    print("Student deleted successfully.")
                elif choice == "5":
                    course_name = input("Course Name: ")
                    credits = int(input("Credits: "))
                    department = input("Department: ")
                    add_course(course_name, credits, department)
                    print("Course added successfully.")
                elif choice == "6":
                    view_courses()
                elif choice == "7":
                    course_id = int(input("Course ID to update: "))
                    course_name = input("Course Name: ")
                    credits = int(input("Credits: "))
                    department = input("Department: ")
                    update_course(course_id, course_name, credits, department)
                    print("Course updated successfully.")
                elif choice == "8":
                    course_id = int(input("Course ID to delete: "))
                    delete_course(course_id)
                    print("Course deleted successfully.")
                elif choice == "9":
                    student_id = int(input("Student ID: "))
                    course_id = int(input("Course ID: "))
                    grade = input("Grade: ")
                    enroll_student(student_id, course_id, grade)
                    print("Student enrolled successfully.")
                elif choice == "10":
                    view_enrollments()
                elif choice == "11":
                    enrollment_id = int(input("Enrollment ID: "))
                    student_id = int(input("Student ID: "))
                    course_id = int(input("Course ID: "))
                    grade = input("Grade: ")
                    update_enrollment(enrollment_id, student_id, course_id, grade)
                    print("Enrollment updated successfully.")
                elif choice == "12":
                    enrollment_id = int(input("Enrollment ID: "))
                    delete_enrollment(enrollment_id)
                    print("Enrollment deleted successfully.")
                else:
                    print("Invalid choice.")

if __name__ == "__main__":
    main()