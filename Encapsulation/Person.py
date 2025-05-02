class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age >= 0:
            self.__age = age
        else:
            self.__age = "Invalid age"

    def display(self):
        print(f"Name: {self.__name}, Age: {self.__age}")


p = Person("raj", 26)
p.display()

p.age = 30
p.name = "mad"

p.display()
