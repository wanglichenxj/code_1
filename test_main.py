import unittest

from main import Student


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


if __name__ == "__main__":
    unittest.main()
