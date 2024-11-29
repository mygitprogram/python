inputfile = open("codingal.txt","r")
outputfile = open("unique.txt","x")
linesofar = set()
for line in inputfile:
    if line not in linesofar:
        outputfile.write(line)
        linesofar.add(line)
inputfile.close()
outputfile.close()

with open("unique.txt","r") as f:
    print(f.read())

f.close()