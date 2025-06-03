
def generate_fibonacci(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        result.append(b)
    return result

def test_fibonacci_output():
    assert generate_fibonacci(5) == [1, 1, 2, 3, 5]

def test_zero_terms():
    assert generate_fibonacci(0) == []

def test_one_term():
    assert generate_fibonacci(1) == [1]
