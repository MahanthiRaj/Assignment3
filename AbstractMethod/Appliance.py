from abc import ABC, abstractmethod

class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

class Fan(Appliance):
    def turn_on(self):
        return "Fan is spinning"

class Light(Appliance):
    def turn_on(self):
        return "Light is glowing"

f = Fan()
l = Light()
print(f.turn_on())
print(l.turn_on())
