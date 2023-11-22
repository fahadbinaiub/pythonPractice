# check a number is odd or even
def new():
    num = int(input("Enter a number: "))
    if num % 2 == 1:
         print("Odd")
    else:
         print("Even")
    print("Do you want to check again? y/n")

    def user():
        check = input()
        if check == "y" or check == "Y":
            new()
        elif check == "n" or check == "N":
            print("Thanks for using")
        else:
            print("Wrong input, please try again!")
            print("Do you want to check again? y/n")
            user()
    user()


new()
