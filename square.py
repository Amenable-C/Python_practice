# Mutiplication Table 제곱
def mul(num1, num2):
    total = 1
    for i in range(0, num2):
        total = total * num1
    return total

while True:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("How many time do it be timed?: "))
    print("The answer: ", mul(num1, num2))
    goOn = input("If you break this service put the '-1' or put the anyword")
    if goOn == '-1':
        break