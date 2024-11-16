# Armstrong number

n = int(input("enter the number"))

num = n
sum = 0

while num !=0:
    rem = num%10
    sum = sum + rem**3
    num = num//10

if sum == n:
    print("the given no is Armstrong number")
else:
    print("the given no is not Armstrong number")
    
    