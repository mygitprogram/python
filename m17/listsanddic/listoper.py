# operation on list
a = ["Apple","Orange","Guava","Mango","Banana","Kiwi"]
print(a,type(a))
print("length of the list",len(a))
print("the first elementof the list",a[0])
a.append("melon")
print(a)
a.remove("Guava")
print(a)
a.sort()
print("sorted list")
print(a)
a.pop()
a.reverse()
print(a)
print("muliplication on a",a*2)
print(a[:4])
a.clear()
print(a)