from app.db import add_student, get_students, get_student, delete_student


def create_student(student_id, name, age, course):
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    add_student(student)
    return student


def show_students():
    return get_students()


def find_student(student_id):
    return get_student(student_id)


def remove_student(student_id):
    return delete_student(student_id)