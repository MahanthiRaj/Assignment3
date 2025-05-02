class Employee:
    def __init__(self, name, salary):
        self.__name = name        # Private
        self.__salary = salary    # Private

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary


e = Employee("Bob", 50000)

print("Name:", e.get_name())
print("Salary:", e.get_salary())

# print(e.__name)  # AttributeError
# print(e.__salary)
