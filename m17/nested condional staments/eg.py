units = int(input("enter the units"))
if units < 50:
    amt = units*2.60 + 25
elif units < 100:
    amt = (50*2.60) +(units-50)*3.25 + 35
elif units < 200:
    amt = (50*2.60) + (50 *3.25) +(units-100)*5.26 + 45
else :
    amt = (50*2.60) + (50 *3.25) + (50*5.26) + (units-100)*8.45 + 75

print("the electricy bill",amt)
