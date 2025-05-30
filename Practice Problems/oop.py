#Inheritance

#single Inheritance

class animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class dog(animal):
    def Dog(self):
        print(self.name,self.age)
        
d = dog("bull",3)
d.Dog()

#multiple Inheritance

class father:
    def __init__(self, father_name):
        self.father_name = father_name
        
class mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name
              
class child:
    def __init__(self,father_name,mother_name ,son_name):
        father.__init__(self, father_name)
        mother.__init__(self, mother_name)
        self.son_name = son_name
    
    def family_names(self):
        print("father name:",self.father_name,"mother name:",self.mother_name,"son name:",self.son_name)
        

fam=child("ram","lakshmi","raj")
fam.family_names()

#multi level heritance

class father:
    def __init__(self, father_name):
        self.father_name = father_name
        
class mother(father):
    def __init__(self,father_name, mother_name):
        father.__init__(self, father_name)
        self.mother_name = mother_name
              
class child(mother):
    def __init__(self,father_name,mother_name ,son_name):
        super().__init__(father_name, mother_name)
        self.son_name = son_name
    
    def family_names(self):
        print("father name:",self.father_name,"mother name:",self.mother_name,"son name:",self.son_name)
        

fam=child("ram","lakshmi","raj")
fam.family_names()

#Hybrid 
class father:
    def __init__(self, father_name):
        self.father_name = father_name
        
class mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name
              
class child:
    def __init__(self,father_name,mother_name ,son_name):
        father.__init__(self, father_name)
        mother.__init__(self, mother_name)
        self.son_name = son_name
        
class child1(child):
    def __init__(self,father_name,mother_name ,son_name, son2_name):
        super().__init__(father_name,mother_name ,son_name)
        self.son2_name = son2_name
    
    def family_names(self):
        print("father name:",self.father_name,"mother name:",self.mother_name,"son name:",self.son_name, "second son name:",self.son2_name)
        

fam=child1("ram","lakshmi","raj","avi")
fam.family_names()