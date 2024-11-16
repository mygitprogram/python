# check the student is eligible to write the exam
mc = input("enter you have a medical cause or not \n1. yes \n2. no")
if mc == "1":
    print("you are eligible to write the exam")
elif mc == "2":
    att = int(input("enter the attendance in percentage"))
    if att > 75:
        print("you are eligible to write the exam")
    else:
        print("you are not eligible")
else:
    print("no a valid input")