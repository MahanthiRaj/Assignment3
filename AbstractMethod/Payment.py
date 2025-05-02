from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class Cash(Payment):
    def pay(self):
        return "Paid with cash"

p = Cash()
print(p.pay())
