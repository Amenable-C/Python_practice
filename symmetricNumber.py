while True:
    numString = input("Enter a number (-1 to quit): ")
    if(int(numString) < 0):
        break
    count = len(numString)

    i = 0
    j = count - 1
    while(i < count):
        if(numString[i] != numString[j]):
            break
        i = i + 1
        j = j - 1

    if(i == count):
        print("Yes,", numString, "is symmetric.")
    else:
        print("No,", numString, "is asymmetric")