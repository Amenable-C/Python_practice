# Prime Number

while True:
    num = int(input("Enter a value (-1 to quit): "))
    if num == -1:
        print("Bye")
        break
    elif num == 1:
        print("Nope")
    elif num == 2:
        print("Yeees!!")
    elif num > 2:
        for i in range(2, num):
            if num % i == 0:
                print("NOPE")
                break
            if i == num-1:
                print("Yeeees")
    else:
        print("Put another number")