# sum of n numbers
x = 1
sum = 0
n = int(input("Enter the last number: "))
while x <= n:
    sum = x + sum
    x = x + 1

print(sum)
