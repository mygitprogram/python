# count lines in the file
colist = []
counter = 0
f1 = open("codingal.txt","r")

content = f1.read()
f1.close()
collist = content.split("\n")

for i in collist:
    if i :
        counter +=1

print("the no of lines in the file",counter)