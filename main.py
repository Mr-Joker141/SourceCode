# Source Code
def calculate_grade(scores):
    grades = []
    for score in scores:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        grades.append(grade)
    return grades

def get_average_score(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)


# Test Code
def test_calculate_grade():
    assert calculate_grade([95, 85, 75, 65, 55]) == ["A", "B", "C", "D", "F"]

def test_get_average_score():
    assert get_average_score([90, 80, 70, 60, 50]) == 70
    assert get_average_score([100, 95, 80, 70, 65]) == 82
    assert get_average_score([50, 60, 70, 80, 90]) == 70
