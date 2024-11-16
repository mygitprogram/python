class car:
    def __init__(self,brand,model):
        self.brand = brand;
        self.model =model;
    def move(self):
        print("we can drive the car")
class boat:
    def __init__(self,brand,model):
        self.brand = brand;
        self.model =model;
    def move(self):
        print("we can sail the boar")
car1 = car("ford","mustang")
boat1 = boat("Ibiza","123")
for x in(car1,boat1):
    print(x.brand,x.model)
    x.move();