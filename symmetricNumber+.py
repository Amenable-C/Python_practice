# Symmetric number

while True:
    num = input("Enter a number (-1 to quit): ")
    if num == '-1':
        break
    dis = len(num)

    for i in range(0, dis):
        if num[i] != num[dis-i-1]:
            print("NOPE")
            break
        if i == (dis-1):
            print("Yeeees!!")
