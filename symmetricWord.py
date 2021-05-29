while True:
    word = input("Enter a number(-1 to quit)")
    if word == "-1":
        break
    dis = len(word)

    for i in range(0, dis):
        if word[i] != word[dis-1-i]:
            print("No, %s is not ~~" %word)
            break
        elif i == dis - 1:
            print("Yes, %s is" %word)


