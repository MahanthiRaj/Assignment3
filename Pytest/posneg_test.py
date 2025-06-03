def check_number(x):
    if x > 0:
        return "Positive Number"
    else:
        return "Negative Number"

def test_positive():
    assert check_number(10) == "Positive Number"
    assert check_number(1) != "Negative Number"

def test_negative():
    assert check_number(-5) == "Negative Number"
    assert check_number(-1) != "Positive Number"
