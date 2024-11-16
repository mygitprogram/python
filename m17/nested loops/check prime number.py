# program to check whether the given no is prime or not
n = int(input("enter the number"))
if n > 1:
    for i in range(2,n):
        if n%i == 0:
            break
    else:
        print("the given number is prime number")