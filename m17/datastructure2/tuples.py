# operation on tuples
tuple1 = (10,20,405,24,20,10)
print(tuple1,type(tuple1))
t1 = (10,30 ,('pink','yellow'),23,45)
print(t1,type(t1))
# acessing tuples
print(tuple1[4])
print(tuple1[-2])

print(t1[2])
print(t1[2][0])
t2 = tuple([23,34,56])
print(t2,type(t2))
l1 = ['john','james']
t3 = tuple(l1)
print(t3,type(t3))
for i in tuple1:
    print(i)