# program to check given no is Armstrong no or not
num = int(input("enter the number"))

sum = 0
temp = num
while temp > 0:
    dig = temp%10
    sum = sum*10 + dig
    temp= temp //10
print(sum)


    