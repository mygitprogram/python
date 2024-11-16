# check whether a number is divisible by another number or not
num1 = float(input("enter the numerator"))
num2 = float(input("enter the denominator"))

if num1%num2 == 0:
    print(f"the {num1} is divisible by {num2}")
else:
    print(f"the {num1} is not divisible by {num2}")