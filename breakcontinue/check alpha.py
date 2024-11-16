def check(str1,a):
    for i in str1:
        if i == a:
            break
    else:
        print("the alphabet is not present")
        return 0
    print(a,"the alphabet is present")
    
str1 = input("enter the string")
a = input("enter the alphabet")
check(str1,a)