file1 = open("codingal.txt","r")
file2 = open("codingalupdated.txt","w")
cont = file1.readlines()
for i in range(1,len(cont)+1):
    if i%2 != 0:
        file2.write(cont[i-1])

file1.close()
file2.close()

file = open("codingalupdated.txt","r")
print(file.read())

file.close()
print()