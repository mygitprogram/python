# convert list to dictionary
def convert(s):
    dic1= {}
    for items in s:
        dic1[items[0]]=items[1:]
    return(dic1)




students = [[1,"john",'v'],[2,'Maria','v'],[3,"james",'vi']]
print(students)
print(convert(students))