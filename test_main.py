import unittest

from main import Student, course_score_variance


class TestStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.student = Student("Alice", "S001", 80.0, 90.0)

    def test_default_scores_are_zero(self) -> None:
        student = Student("Bob", "S002")
        self.assertEqual(student.scores(), {"english": 0.0, "math": 0.0})
        self.assertEqual(student.total_score(), 0.0)
        self.assertEqual(student.average_score(), 0.0)

    def test_scores(self) -> None:
        self.assertEqual(
            self.student.scores(),
            {"english": 80.0, "math": 90.0},
        )

    def test_total_score(self) -> None:
        self.assertEqual(self.student.total_score(), 170.0)

    def test_average_score(self) -> None:
        self.assertEqual(self.student.average_score(), 85.0)

    def test_format_scores_contains_fields(self) -> None:
        text = self.student.format_scores()
        self.assertIn("Alice", text)
        self.assertIn("S001", text)
        self.assertIn("80.0", text)
        self.assertIn("90.0", text)
        self.assertIn("170.0", text)
        self.assertIn("85.0", text)


class TestCourseScoreVariance(unittest.TestCase):
    def test_english_variance(self) -> None:
        students = [
            Student("A", "1", 80.0, 0.0),
            Student("B", "2", 90.0, 0.0),
        ]
        self.assertEqual(course_score_variance(students, "english"), 25.0)

    def test_math_variance(self) -> None:
        students = [
            Student("A", "1", 0.0, 70.0),
            Student("B", "2", 0.0, 80.0),
            Student("C", "3", 0.0, 90.0),
        ]
        self.assertAlmostEqual(course_score_variance(students, "math"), 200 / 3)

    def test_single_student_variance_is_zero(self) -> None:
        students = [Student("A", "1", 88.0, 92.0)]
        self.assertEqual(course_score_variance(students, "english"), 0.0)

    def test_course_name_case_insensitive(self) -> None:
        students = [
            Student("A", "1", 10.0, 0.0),
            Student("B", "2", 20.0, 0.0),
        ]
        self.assertEqual(course_score_variance(students, "English"), 25.0)

    def test_unknown_course_raises(self) -> None:
        with self.assertRaises(ValueError):
            course_score_variance([Student("A", "1")], "science")

    def test_empty_students_raises(self) -> None:
        with self.assertRaises(ValueError):
            course_score_variance([], "english")


if __name__ == "__main__":
    unittest.main()
