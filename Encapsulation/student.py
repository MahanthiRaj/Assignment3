class Student:
    def __init__(self, roll, name, marks):
        self.rollNumber = roll
        self.name = name
        self.__marks = marks
        print("student roll", self.rollNumber, "Student name:", self.name)

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):
        if value >= 0:
            self.__marks = value
        else:
            self.__marks = "Marks can't be negative."


student = Student(1, "Bob", 90)
print("Student's marks:", student.marks)

student.marks = -5
student.marks = 95
print("Updated marks:", student.marks)
