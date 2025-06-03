def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def test_grades():
    assert get_grade(95) == "A"
    assert get_grade(85) == "B"
    assert get_grade(75) == "C"
    assert get_grade(65) == "D"
    assert get_grade(50) == "F"

    assert get_grade(65) != "A"
    assert get_grade(50) != "B"
