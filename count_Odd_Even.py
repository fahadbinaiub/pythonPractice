#count even or odd numbers in a series of numbers

num = [1,2,3,4,5,6,7,8,9]
odd_count = 0
even_count = 0
for x in num:
    if x % 2 == 0:
        even_count = even_count + 1
    elif x % 2 != 0:
        odd_count = odd_count + 1

print(even_count)
print(odd_count)