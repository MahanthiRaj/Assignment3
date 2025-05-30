class Private:
    def __init__(self):
        self.__salary=100
    def salary(self):
        return self.__salary
    
s2 = Private()
print(s2.salary())