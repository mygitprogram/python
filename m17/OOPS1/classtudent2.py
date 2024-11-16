class student:
    name = "john"
    age = 14
    def intro(self):
        print("I am a student")
    def details(self):
        print("My name is",self.name)
        print("My age is",self.age)

student1 = student()
student1.intro()
student1.details()
    