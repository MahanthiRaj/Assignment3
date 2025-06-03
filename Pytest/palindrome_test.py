def is_palindrome(s):
    return s == s[::-1]

def test_palindrome_true():
    assert is_palindrome("madam") is True

def test_palindrome_false():
    assert is_palindrome("hello") is False

def test_empty_string():
    assert is_palindrome("") is True
