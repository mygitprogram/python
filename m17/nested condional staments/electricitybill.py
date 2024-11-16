# calculate electricity bill

units = int(input("enter the units"))
if units <= 50:
    amt = units * 2.60 + 25
elif units <= 100:
    amt = (units-50) * 3.20 + (50 * 2.60) + 35
elif units <= 200:
    amt = (units-100) * 5.26 + (50 * 2.60) + (50 *3.20) + 45
else:
    amt = (units-200) * 8.45 + (50 * 2.60) + (50 *3.20) + (100*5.26)+ 75

print("the electricity charge is ",amt)
