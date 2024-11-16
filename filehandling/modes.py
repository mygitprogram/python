# opening the files in all the modes, "r", "w", "a"

f = open("codingal.txt","r")
print(f.read())
f.close()

f = open("codingal.txt","w")
f.write("I am penguin, I am 2 yr old")
f.close()

f = open("codingal.txt","r")
print(f.read())
f.close()

f = open("codingal.txt","a")
f.write("I made kids to love with coding")
f.close()

f = open("codingal.txt","r")
print(f.read())
f.close()