
file1 = open("codingal.txt","r")
file2 = open("codingalupdated.txt","w")

for lines in file1.readlines():
    if not(lines.startswith("Codingal")):
        print(lines)
        file2.write(lines)

file1.close()
file2.close()