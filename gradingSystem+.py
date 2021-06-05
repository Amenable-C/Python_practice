# Grading System // 2nd trial
def high(num_list):
    high = int(num_list[0])
    for a in num_list:
        if int(a) >= high:
            high = int(a)
    return high

def low(num_list):
    low = int(num_list[0])
    for a in num_list:
        if int(a) <= low:
            low = int(a)
    return low

def ave(num_list):
    sum = 0
    for a in num_list:
        sum = sum + int(a)
    return sum / len(num_list)



num_list = []
while True:
    num = input("Enter a score(-1 to quit): ")
    if num == '-1':
        break
    num_list.append(num)



while True:
    choose = int(input("Menu: 1. highest 2. lowest 3. ave 4. quit"))
    if choose == 1:
        print(high(num_list))
    elif choose == 2:
        print(low(num_list))
    elif choose == 3:
        print(ave(num_list))
    else:
        print("Bye")
        break

