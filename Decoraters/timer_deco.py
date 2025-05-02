import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Time taken:", end - start)
    return wrapper

@timer
def add_two_numbers():
    result = 10 + 20
    print("Result of addition:", result)

add_two_numbers()
