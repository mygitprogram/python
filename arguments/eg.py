def recurse(n):
    if n == 0:
        return ""
    str1 = "best wishes "
    return str1 + str(recurse(n-1))
    
print(recurse(5))