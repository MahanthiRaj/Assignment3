# 1. Person and Employee classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

emp = Employee("Alice", 30, 50000)
emp.display()

# 2. Animal and Dog classes
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")
        
dog = Dog()
dog.speak()

# 3. Vehicle and Car classes
class Vehicle:
    def info(self):
        print("This is a vehicle")

class Car(Vehicle):
    def brand(self, brand_name):
        print(f"Brand: {brand_name}")
            

car = Car()
car.info()
car.brand("Toyota")

# 4. Shape and Square classes
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
    
sq = Square(4)
print("Area of square:", sq.area())

# 5. Parent and Child with private variable
class Parent:
    def __init__(self):
        self.__secret = "Private Info"

    def get_secret(self):
        return self.__secret

class Child(Parent):
    def show_secret(self):
        print("Secret:", self.get_secret())


child = Child()
child.show_secret()


#Multiple Inheritance
#1. Create two classes Writer and Editor, each with a method role(). Inherit a class Author from both and override role() to describe an author’s combined role.

class Writer:
    def role(self):
        print("Writes content")

class Editor:
    def role(self):
        print("Edits content")

class Author(Writer, Editor):
    def role(self):
        print("Writes and edits content as an author")
        
author = Author()
author.role()