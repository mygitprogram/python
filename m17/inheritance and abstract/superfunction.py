class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def display(self):
        print(self.fname,self.lname)
class employee(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.year =year
        
    def displayemp(self):
        print(self.year)
emp1 = employee("Ajay","sharma",2007)
emp1.display()
emp1.displayemp()
print(emp1.year)