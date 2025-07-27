year = int(input("which year you want to check? "))
num=0
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
            num=1
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
    
# check if it is a leap year enter month.
month = int(input("enter a month number from 1 to 12"))
days_in_month = 0
if month in [1, 3, 5, 7, 8, 10, 12]:
    days_in_month = 31
elif month in [4, 6, 9, 11, ]:
    days_in_month = 30
elif month==2:
    if num==1:
        days_in_month = 29
    else:
        days_in_month = 28

print(f"number of {days_in_month}")