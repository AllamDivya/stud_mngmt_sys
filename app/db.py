students = []


def add_student(student):
    students.append(student)
    return True


def get_students():
    return students


def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def delete_student(student_id):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return True
    return False