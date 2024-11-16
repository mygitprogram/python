class person:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def display(self):
        print(self.name,self.id)
class employee(person):
    def __init__(self,name,id,salary,post):
        person.__init__(self,name,id)
        self.salary =salary
        self.post = post
    def displayemp(self):
        print(self.salary,self.post)
emp1 = employee("Ajay",112,50000,'engineer')
emp1.display()
emp1.displayemp()

        