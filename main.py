"""Student score tracking and simple class-level statistics."""

from statistics import pvariance


class Student:
    """A student with identity fields and scores for English and Math."""

    def __init__(
        self,
        name: str,
        student_id: str,
        english_score: float = 0.0,
        math_score: float = 0.0,
    ) -> None:
        self.name = name
        self.student_id = student_id
        # Scores default to 0 until grades are recorded.
        self.english_score = english_score
        self.math_score = math_score

    def scores(self) -> dict[str, float]:
        """Return per-course scores keyed by course name."""
        return {"english": self.english_score, "math": self.math_score}

    def total_score(self) -> float:
        """Sum of English and Math scores."""
        return self.english_score + self.math_score

    def average_score(self) -> float:
        """Mean of the two course scores."""
        return self.total_score() / 2

    def format_scores(self) -> str:
        """Human-readable summary for printing or logging."""
        s = self.scores()
        return (
            f"Student: {self.name} (ID: {self.student_id})\n"
            f"English: {s['english']}, Math: {s['math']}\n"
            f"Total: {self.total_score()}, Average: {self.average_score()}"
        )


def course_score_variance(students: list[Student], course: str) -> float:
    """Population variance of scores for the given course across students.

    Args:
        students: Cohort to analyze; must be non-empty.
        course: ``"english"`` or ``"math"`` (case-insensitive).

    Returns:
        Population variance (divide by N, not N - 1).
    """
    course_key = course.lower()
    if course_key not in ("english", "math"):
        raise ValueError(f"Unknown course: {course}")
    if not students:
        raise ValueError("students must not be empty")

    scores = [student.scores()[course_key] for student in students]
    return pvariance(scores)


if __name__ == "__main__":
    # Quick demo when running this file directly.
    student = Student("Alice", "S001", 88.0, 92.0)
    print(student.format_scores())
