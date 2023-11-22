# leap year check program
year = int(input("Enter your year: "))
if year % 400 == 0:
    print("This is a leap year!")
elif year % 100 == 0:
    print("This is not a leap year!")
elif year % 4 == 0:
    print("This is a leap year!")
else:
    print("This is not a leap year")