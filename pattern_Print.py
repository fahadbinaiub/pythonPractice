# pattern printing
n = int(input("Enter row number of the pattern : "))
star = "*"
for x in range(1,n+1,1):
    print(x*star)
for i in range(n-1, 0, -1):
    for j in range(0, i):
        print(star, end = "")
    print("\r")
