class Student:
    def __init__(
        self,
        name: str,
        student_id: str,
        english_score: float = 0.0,
        math_score: float = 0.0,
    ) -> None:
        self.name = name
        self.student_id = student_id
        self.english_score = english_score
        self.math_score = math_score

    def scores(self) -> dict[str, float]:
        return {"english": self.english_score, "math": self.math_score}

    def total_score(self) -> float:
        return self.english_score + self.math_score

    def average_score(self) -> float:
        return self.total_score() / 2

    def format_scores(self) -> str:
        s = self.scores()
        return (
            f"Student: {self.name} (ID: {self.student_id})\n"
            f"English: {s['english']}, Math: {s['math']}\n"
            f"Total: {self.total_score()}, Average: {self.average_score()}"
        )


if __name__ == "__main__":
    student = Student("Alice", "S001", 88.0, 92.0)
    print(student.format_scores())
