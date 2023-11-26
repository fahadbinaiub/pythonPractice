# n + nn + nnn + ......
n = int(input("Enter the number: "))
multiple = 1
sum = 0

for x in range(3):
    multiple = multiple * n
    sum = multiple + sum
print("The summation is: ",sum)
