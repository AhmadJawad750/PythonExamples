print ("welcome to tip calculator")

bill=float(input("what is the total bill amount ?/n PKR"))
tip=int(input("how much tip will you like to  give \n Percent"))
split = int(input("How many people to split the bill?\nPeople:"))
total = ("{:.2f}".format((((bill * (tip / 100)) + bill) / split)))
print(f"Each person should pay: PKR {total}")