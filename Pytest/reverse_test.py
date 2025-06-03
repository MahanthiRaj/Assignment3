def reverse_string(s):
    if type(s) != str:
        raise ValueError("Input must be a string")
    return s[::-1]

def test_reverse_normal():
    assert reverse_string("hello") == "olleh"

def test_reverse_empty():
    assert reverse_string("") == ""

def test_reverse_palindrome():
    assert reverse_string("madam") == "madam"

def test_reverse_invalid_type():
    import pytest
    with pytest.raises(ValueError):
        reverse_string(123)
