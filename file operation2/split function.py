# open a file using with and split the lines in the file

with open("codingal.txt","w") as file1:
    file1.write("Hello World")
file1.close()
list1 =[]
with open("codingalupdated.txt","r") as file1:
    data = file1.readlines()
    for line in data:
        word = line.split()
        list1.append(word)
file1.close()
print(list1)