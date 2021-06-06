# Staticstics S/W
def scores(num_list):
    what = int(input("Which ?? "))
    return num_list[what-1]

def high(num_list):
    sorted(num_list)
    return num_list[len(num_list)-1]

def low(num_list):
    sorted(num_list)
    return num_list[0]

def ave(num_list):
    sum = 0
    for i in num_list:
        sum = sum + i
    return sum / len(num_list)

def mid(num_list):
    if len(num_list) % 2 == 1:
        mid = len(num_list) // 2
        return num_list[mid]
    elif len(num_list) % 2 == 0:
        mid = (len(num_list) // 2) - 1
        re = (num_list[mid] + num_list[mid + 1]) // 2
        return re






num_list = []
while True:
    num = int(input("Put the score (-1 to quit): "))
    if num == -1:
        break
    num_list.append(num)

while True:
    menu = int(input("1. scores 2. highest 3. lowest 4. ave 5. mid 6. quit // choice >> "))
    if menu == 6:
        break
    elif menu == 1:
        print(scores(num_list))
    elif menu == 2:
        print(high(num_list))
    elif menu == 3:
        print(low(num_list))
    elif menu == 4:
        print(ave(num_list))
    elif menu == 5:
        print(mid(num_list))
