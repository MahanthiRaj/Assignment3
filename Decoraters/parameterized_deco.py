def parameterized_decorator(message):
    def decorator(func):
        def wrapper():
            print(message)
            return func()
        return wrapper
    return decorator

@parameterized_decorator("This is a custom message")

def hello():
    return "Hello World!"

print(hello())
