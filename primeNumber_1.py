#prime Number
while (True):
    num = int(input("Enter a value (-1 to quit): "))
    if(num < 0):
        break
    checkNum = 2
    while (checkNum < num):
        if(num % checkNum == 0):
            break
        checkNum = checkNum + 1

    if(checkNum == num):
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")

print("Bye!")