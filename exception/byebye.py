# write a program to check the number is divided by two, if it is run for an infinite loop.

try :
    n = int(input("enter the number"))
    if n %2 == 0:
        while True:
            print("bye bye")
    else:
        print(n, "the number is not divided by 2")
except ValueError:
    print("the input is wrong")