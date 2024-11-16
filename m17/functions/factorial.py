# factorial using recursion
def fact(n):
    if n==1:
        return 1
    else :
        return n * fact(n-1)

n = int(input("enter the number"))
if n < 0:
    print("for negative numbers no factorial")
elif n == 0:
    print("the factorial is 1")
else:
    print("the factorial of the ",n ,"is",fact(n))