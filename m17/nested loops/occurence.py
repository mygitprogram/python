# find the occurance of a character in a given string
str1 = input("enter a string")
ch = input("enter a character")
count = 0
for i in str1:
    if i.lower() == ch.lower():
        count+=1

print("The occurance of a character",count)