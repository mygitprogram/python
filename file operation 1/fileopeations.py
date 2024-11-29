# file operation
# read
file = open("codingal.txt","r")
print(file.read())
file.close()
# write
file = open("codingal.txt","w")
file.write("this is a new file")
file.close()

# append
file = open("codingal.txt","a")
file.write("this is the entire content of the file")
file.close()