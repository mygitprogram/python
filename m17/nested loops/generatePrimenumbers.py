# to print all the prime numbers between a given range
l = int(input("enter the lower limit"))
u = int(input("enter the upper limit"))

for i in range(l,u+1):
    
    for j in range(2,i):
        if i%j == 0:
            
            break;
    else:
        print(i)