# Enscapsulation

class Aeroplane:
    def __init__(self):
        self.__brand = "Air India"
    
    def __fly(self):
        print(self.__brand,"is flying")
    
    def info(self):
        self.__fly()

A1 = Aeroplane();
A1.info()
A1.__brand = "jet airways"
A1.info()
    