class Student:
    def __init__(self, name, age):
        self.name = name  # Public
        self.age = age    # Public

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


s = Student("Alice", 20)
s.display()

print(s.name)
print(s.age)
s.display()