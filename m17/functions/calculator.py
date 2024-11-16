def addition(x,y):
    return x +y

def sub(x,y):
    return x -y

def mul(x,y):
    return x *y

def div(x,y):
    return x /y

x = float(input("enter the first value"))
y = float(input("enter the first value"))

print(f"the addition of {x} and {y} is {addition(x,y)}")
print(f"the subtraction of {x} and {y} is {sub(x,y)}")
print(f"the multiplication of {x} and {y} is {mul(x,y)}")
print(f"the division of {x} and {y} is {div(x,y)}")