c = input("enter a character")
if len(c)>1:
    print("\nInvalid Input!")
else:
    if c>='a' and c<='z':
        print("\n\"" +c+ "\" is an alphabet.")
    elif c>='A' and c<='Z':
        print("\n\"" +c+ "\" is an alphabet.")
    else:
        print("\n\"" +c+ "\" is not an alphabet!")