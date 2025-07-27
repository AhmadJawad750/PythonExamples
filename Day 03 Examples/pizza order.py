print("welcome to abc pizza ordering shop")

size = input("What size pizza do you want? S, M, or L? ")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid size! Please choose S, M, or L.")
    # Agar user ghalat size dale to aage ka code na chalay
    exit() 

extra_cheese = input("Do you want extra cheese? Y or N? ")
if extra_cheese == "Y":
    bill += 1

extra_toppings = input("Do you want extra toppings like mushrooms")
if extra_toppings == "Y":
  bill += 2
print(f"Your final bill is PKR {bill}.")
