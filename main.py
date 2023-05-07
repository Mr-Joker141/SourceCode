# Source Code
def calculate_grade(score):
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
    return grade

def get_average_score(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)


# Test Code
def test_calculate_grade():
    assert calculate_grade(95) == "A"
    assert calculate_grade(85) == "B"
    assert calculate_grade(75) == "C"
    assert calculate_grade(65) == "D"
    assert calculate_grade(55) == "F"

def test_get_average_score():
    assert get_average_score([90, 80, 70, 60, 50]) == 70
    assert get_average_score([100, 95, 80, 70, 65]) == 82
    assert get_average_score([50, 60, 70, 80, 90]) == 70
