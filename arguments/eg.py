def factorial(n):
    '''This is a recursive function to find the factorial'''
    if n == 0:
        return 1
    else:
        
        return n * factorial(n-1)
print(factorial.__doc__)   
print("the factorial is :",factorial(5))
