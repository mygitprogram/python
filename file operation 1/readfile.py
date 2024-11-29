# read file

file = open("codingal.txt","r")
print(file.read())

file.close()
print()
# first 8 chararcter

file = open("codingal.txt","r")
print(file.read(8))

file.close()

# append

file = open("codingal.txt","a")
print(file.write("This is in append mode, and I am going to append"))

file.close()