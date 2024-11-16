from abc import ABC,abstractmethod
class vehicle(ABC):
    @ abstractmethod 
    def go():
        pass
class car(vehicle):
    def go(self):
        print("the car is going")
car1 = car()
car1.go()
    