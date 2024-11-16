class parrot:
    species = "bird"
    def __init__(self,name1,age1):
        self.name = name1
        self.age = age1

parrot1 = parrot("candy",2)
parrot2 = parrot("Rudy",3)

print("the species of the parrot1",parrot1.species)
print(f"my name is {parrot1.name} and my age is {parrot1.age}")

print("the species of the parrot2",parrot2.species)
print(f"my name is {parrot2.name} and my age is {parrot2.age}")