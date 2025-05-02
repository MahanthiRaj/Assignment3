class Vehicle:
    def __init__(self, brand):
        self._brand = brand  # Protected

    def show(self):
        print("Vehicle brand:", self._brand)

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_details(self):
        print(f"Car brand: {self._brand}, Model: {self.model}")


c = Car("Toyota", "Camry")
c.show_details()


