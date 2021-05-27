#Input Exception Handling
x = 5
while True:
    try:
        y = int(input("Input a number: "))
    except:
        print("input again!")
    else:
        break
print(x+y)