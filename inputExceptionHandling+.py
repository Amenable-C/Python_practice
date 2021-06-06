x = 5
while True:
    try:
        y = int(input("Input a number(-1 to quit): "))
        if y == -1:
            break
    except Exception as e:
        print(e)
        print("Input again!")
    else:
        print(x+y)
