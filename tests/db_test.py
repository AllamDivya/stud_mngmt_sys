import unittest

from app import db


class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.students.clear()

    def test_add_student(self):
        student = {
            "id": 1,
            "name": "Priya",
            "age": 21,
            "course": "B.Tech"
        }

        result = db.add_student(student)

        self.assertTrue(result)
        self.assertEqual(len(db.students), 1)

    def test_get_students(self):
        student = {
            "id": 1,
            "name": "Priya",
            "age": 21,
            "course": "B.Tech"
        }

        db.add_student(student)

        students = db.get_students()

        self.assertEqual(len(students), 1)

    def test_get_student(self):
        student = {
            "id": 1,
            "name": "Priya",
            "age": 21,
            "course": "B.Tech"
        }

        db.add_student(student)

        result = db.get_student(1)

        self.assertEqual(result["name"], "Priya")

    def test_delete_student(self):
        student = {
            "id": 1,
            "name": "Priya",
            "age": 21,
            "course": "B.Tech"
        }

        db.add_student(student)

        result = db.delete_student(1)

        self.assertTrue(result)
        self.assertEqual(len(db.students), 0)


if __name__ == "__main__":
    unittest.main()