def gmail(n):
    if ".com" in n and "@" in n:
        return True
    else:
        return False

def test_valid_gmail():
    assert gmail("example@gmail.com") is True
    assert gmail("user.name@domain.com") is True

def test_missing_dotcom():
    assert gmail("example@gmail") is False

def test_empty_string():
    assert gmail("") is False
