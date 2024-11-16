# calculator

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

choice = input("1. Addition \n2.Subtraction \n3.Multiplication \n4.Division \nenter your choice")

if choice == "1":
    a = int(input("enter the number"))
    b = int(input("enter the number"))
    print(f"the sum of two number {a} and {b} is {add(a,b)}")
elif choice == "2":
    a = int(input("enter the number"))
    b = int(input("enter the number"))
    print(f"the sum of two number {a} and {b} is {sub(a,b)}")
elif choice == "3":
    a = int(input("enter the number"))
    b = int(input("enter the number"))
    print(f"the sum of two number {a} and {b} is {mul(a,b)}")
elif choice == "4":
    a = int(input("enter the number"))
    b = int(input("enter the number"))
    print(f"the sum of two number {a} and {b} is {div(a,b)}")
else:
    print("wrong input")

