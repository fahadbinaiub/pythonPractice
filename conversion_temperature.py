# coversion of temperatures
user = int(input("Which conversion do you want to do? \n1. Celsius to fahrenheit\n2. Fahrenheit to celsius\n"))
if user == 1:
    cel = int(input("Enter the celsius value: "))
    far = (9/5) * (cel + 32)
    print(far)
elif user == 2:
    far = int(input("Enter the fahrenheit value: "))
    cel = (5/9)* (far - 32)
    print(cel)
else:
    print("Restart!")