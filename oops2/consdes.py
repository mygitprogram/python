class employee:
    def __init__(self):
        print("constructor called")
    
    def __del__(self):
        print("destructor called")


e1 = employee()
e2 = employee()
print("body of the loop")
del e1
print("e1 object deleted")
del e2
print("e2 object deleted")

