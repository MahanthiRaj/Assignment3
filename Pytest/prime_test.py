def is_prime_simple(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        return True

def test_not_prime():
    assert is_prime_simple(1) is False
    assert is_prime_simple(0) is False
    assert is_prime_simple(9) is False  # 9 is not a prime (divisible by 3)

def test_prime():
    assert is_prime_simple(2) is True
    assert is_prime_simple(3) is True
