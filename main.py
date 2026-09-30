from app.stud_ser import (
    create_student,
    show_students,
    find_student,
    remove_student
)


def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            course = input("Enter course: ")

            create_student(student_id, name, age, course)
            print("Student added successfully!")

        elif choice == "2":
            students = show_students()

            if not students:
                print("No students found.")
            else:
                for student in students:
                    print(student)

        elif choice == "3":
            student_id = int(input("Enter student ID: "))
            student = find_student(student_id)

            if student:
                print("Student found:")
                print(student)
            else:
                print("Student not found.")

        elif choice == "4":
            student_id = int(input("Enter student ID: "))

            if remove_student(student_id):
                print("Student deleted successfully!")
            else:
                print("Student not found.")

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()