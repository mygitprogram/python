# file operation in x mode and using OS module

with open("codingal2.txt","x") as file1:
    file1.write("Hello penguin")
file1.close()

import os
if os.path.exists("codingal1.txt") :
    os.remove("codingal1.txt")
else :
    print("file does not exists")

os.remove("codingal2.txt")
os.rmdir("folder")