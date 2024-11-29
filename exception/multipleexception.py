try:
    a, b = eval(input("enter the number separated by commas"))
    ans = a/b
    print("the result is",ans)
except ZeroDivisionError:
    print("the mumber cannot divided by zero")

except SyntaxError:
    print("You missed comma")

except :
    print("error occured")
else :
    print("no exception")
finally :
    print("however this will statement is executed")