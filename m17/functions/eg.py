def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

op = input("\n1. Addition \n2.Subtraction \n3.Multiplicaiton \n4.Division \nEnter your choice")
if op == "1":
    a = int(input("enter the number1"))
    b = int(input("enter the second number"))
    print("{0} + {1} = {2}".format(a,b,add(a,b)))
elif op == "2":
    a = int(input("enter the number1"))
    b = int(input("enter the second number"))
    print("{0} - {1} = {2}".format(a,b,sub(a,b)))
elif op == "3":
    a = int(input("enter the number1"))
    b = int(input("enter the second number"))
    print("{0} * {1} = {2}".format(a,b,mul(a,b)))
elif op == "4":
    a = int(input("enter the number1"))
    b = int(input("enter the second number"))
    print("{0} / {1} = {2}".format(a,b,div(a,b)))
else:
    print("wrong input")