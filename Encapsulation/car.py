class Car:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.__speed = speed
        
        print("brand name:", self.__brand, "model name:", self.__model)

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if 0 <= value <= 200:
            self.__speed = value
        else:
            self.__speed = "Speed must be between 0 and 200."


car = Car("Toyota", "Corolla")

car.speed = 220
print("Car speed:", car.speed)
