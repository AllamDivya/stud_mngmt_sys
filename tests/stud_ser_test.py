import unittest

from app.stud_ser import (
    create_student,
    show_students,
    find_student,
    remove_student
)


class TestStudentService(unittest.TestCase):

    def setUp(self):
        from app import db
        db.students.clear()

    def test_create_student(self):
        student = create_student(1, "Rahul", 20, "B.Tech")

        self.assertEqual(student["id"], 1)
        self.assertEqual(student["name"], "Rahul")

    def test_show_students(self):
        create_student(1, "Rahul", 20, "B.Tech")
        students = show_students()

        self.assertEqual(len(students), 1)

    def test_find_student(self):
        create_student(1, "Rahul", 20, "B.Tech")

        student = find_student(1)

        self.assertIsNotNone(student)
        self.assertEqual(student["name"], "Rahul")

    def test_remove_student(self):
        create_student(1, "Rahul", 20, "B.Tech")

        result = remove_student(1)

        self.assertTrue(result)
        self.assertIsNone(find_student(1))


if __name__ == "__main__":
    unittest.main()