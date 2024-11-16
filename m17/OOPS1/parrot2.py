class parrot:
    species = "bird"
    def __init__(self,name1,age1):
        self.name = name1
        self.age = age1
    def sing(self,sing1):
        return  "my name is " + self.name + "my age is  " + str(self.age) + " I can sing" +sing1
    def dance(self,d):
        return  "my name is " + self.name + "my age is  " + str(self.age) + " I can dance" +d

parrot1 = parrot("candy",2)



print(parrot1.sing("rock"))
print(parrot1.dance("western"))