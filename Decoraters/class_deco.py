class MyClass:
    name = "MyClass"
    
    @classmethod
    def class_greet(cls):
        return f"Hello from {cls.name}!"

print(MyClass.class_greet())
